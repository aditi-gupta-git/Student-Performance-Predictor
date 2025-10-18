#!/usr/bin/env python3
"""
Test runner script for the Student Performance Predictor project.
"""

import subprocess
import sys
import os

def run_tests():
    """Run all tests in the tests directory."""
    print("🧪 Running tests for Student Performance Predictor...")
    print("=" * 50)
    
    # Change to the project root directory
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)
    
    try:
        # Run pytest with verbose output
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "tests/", 
            "-v", 
            "--tb=short",
            "--color=yes"
        ], check=True)
        
        print("\n✅ All tests passed successfully!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Tests failed with exit code {e.returncode}")
        return False
    except FileNotFoundError:
        print("\n❌ pytest not found. Please install it with: pip install pytest")
        return False

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)