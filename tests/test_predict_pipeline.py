import unittest
import pandas as pd
import numpy as np
import sys
import os

# Add the src directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from pipeline.predict_pipeline import CustomData, PredictPipeline

class TestCustomData(unittest.TestCase):
    """Test cases for CustomData class"""
    
    def setUp(self):
        """Set up test data"""
        self.test_data = CustomData(
            gender="female",
            race_ethnicity="group A",
            parental_level_of_education="bachelor's degree",
            lunch="standard",
            test_preparation_course="completed",
            reading_score=85,
            writing_score=90
        )
    
    def test_custom_data_initialization(self):
        """Test CustomData initialization"""
        self.assertEqual(self.test_data.gender, "female")
        self.assertEqual(self.test_data.race_ethnicity, "group A")
        self.assertEqual(self.test_data.parental_level_of_education, "bachelor's degree")
        self.assertEqual(self.test_data.lunch, "standard")
        self.assertEqual(self.test_data.test_preparation_course, "completed")
        self.assertEqual(self.test_data.reading_score, 85)
        self.assertEqual(self.test_data.writing_score, 90)
    
    def test_get_data_as_data_frame(self):
        """Test get_data_as_data_frame method"""
        df = self.test_data.get_data_as_data_frame()
        
        # Check if it returns a DataFrame
        self.assertIsInstance(df, pd.DataFrame)
        
        # Check if it has the correct columns
        expected_columns = [
            "gender", "race_ethnicity", "parental_level_of_education",
            "lunch", "test_preparation_course", "reading_score", "writing_score"
        ]
        self.assertEqual(list(df.columns), expected_columns)
        
        # Check if it has one row
        self.assertEqual(len(df), 1)
        
        # Check values
        self.assertEqual(df.iloc[0]['gender'], "female")
        self.assertEqual(df.iloc[0]['race_ethnicity'], "group A")
        self.assertEqual(df.iloc[0]['parental_level_of_education'], "bachelor's degree")
        self.assertEqual(df.iloc[0]['lunch'], "standard")
        self.assertEqual(df.iloc[0]['test_preparation_course'], "completed")
        self.assertEqual(df.iloc[0]['reading_score'], 85)
        self.assertEqual(df.iloc[0]['writing_score'], 90)

class TestPredictPipeline(unittest.TestCase):
    """Test cases for PredictPipeline class"""
    
    def setUp(self):
        """Set up test data"""
        self.predict_pipeline = PredictPipeline()
        
        # Create test data
        self.test_data = CustomData(
            gender="male",
            race_ethnicity="group B",
            parental_level_of_education="high school",
            lunch="free/reduced",
            test_preparation_course="none",
            reading_score=70,
            writing_score=75
        )
    
    def test_predict_pipeline_initialization(self):
        """Test PredictPipeline initialization"""
        self.assertIsInstance(self.predict_pipeline, PredictPipeline)
    
    def test_predict_with_valid_data(self):
        """Test prediction with valid data"""
        try:
            df = self.test_data.get_data_as_data_frame()
            result = self.predict_pipeline.predict(df)
            
            # Check if result is a numpy array or list
            self.assertTrue(isinstance(result, (np.ndarray, list)))
            
            # Check if result has at least one prediction
            self.assertGreater(len(result), 0)
            
            # Check if prediction is a number
            self.assertTrue(isinstance(result[0], (int, float, np.number)))
            
            print(f"Test prediction result: {result[0]}")
            
        except FileNotFoundError:
            self.skipTest("Model files not found. Run training first.")
        except Exception as e:
            self.fail(f"Prediction failed with error: {str(e)}")

if __name__ == '__main__':
    unittest.main()