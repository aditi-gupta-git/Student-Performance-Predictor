#!/usr/bin/env python3
"""
Simple test script for the Student Performance Predictor API
"""

import requests
import json
import sys

def test_health_endpoint(base_url):
    """Test the health check endpoint"""
    try:
        response = requests.get(f"{base_url}/api/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            return True
        else:
            print(f"❌ Health check failed with status {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_prediction_endpoint(base_url):
    """Test the prediction API endpoint"""
    test_data = {
        "gender": "female",
        "race_ethnicity": "group B",
        "parental_level_of_education": "bachelor's degree",
        "lunch": "standard",
        "test_preparation_course": "completed",
        "reading_score": 85,
        "writing_score": 82
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/predict",
            json=test_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            result = response.json()
            prediction = result.get('prediction')
            if prediction is not None and isinstance(prediction, (int, float)):
                print(f"✅ Prediction API test passed: {prediction}")
                return True
            else:
                print(f"❌ Invalid prediction response: {result}")
                return False
        else:
            print(f"❌ Prediction API failed with status {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Prediction API test failed: {e}")
        return False

def test_validation_errors(base_url):
    """Test API validation with invalid data"""
    # Test missing fields
    invalid_data = {
        "gender": "female",
        "race_ethnicity": "group B"
        # Missing other required fields
    }
    
    try:
        response = requests.post(
            f"{base_url}/api/predict",
            json=invalid_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 400:
            print("✅ Validation error handling works correctly")
            return True
        else:
            print(f"❌ Expected 400 status code, got {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Validation test failed: {e}")
        return False

def main():
    if len(sys.argv) > 1:
        base_url = sys.argv[1].rstrip('/')
    else:
        base_url = "http://localhost:5000"
    
    print(f"Testing Student Performance Predictor API at {base_url}")
    print("=" * 60)
    
    tests = [
        test_health_endpoint,
        test_prediction_endpoint,
        test_validation_errors
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test(base_url):
            passed += 1
        print()
    
    print("=" * 60)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed!")
        sys.exit(0)
    else:
        print("❌ Some tests failed")
        sys.exit(1)

if __name__ == "__main__":
    main()