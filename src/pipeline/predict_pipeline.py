import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os


class PredictPipeline:
    """
    A pipeline for making predictions using a trained machine learning model.
    
    This class handles loading the trained model and preprocessor, then uses them
    to make predictions on new data.
    """
    
    def __init__(self):
        """
        Initialize the PredictPipeline.
        """
        pass

    def predict(self, features):
        """
        Make predictions on the given features.
        
        Args:
            features (pd.DataFrame): Input features for prediction
            
        Returns:
            np.ndarray: Predicted values
            
        Raises:
            CustomException: If prediction fails
        """
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            
            print("Loading model and preprocessor...")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("Model and preprocessor loaded successfully")
            
            # Transform features using the preprocessor
            data_scaled = preprocessor.transform(features)
            
            # Make predictions
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)



class CustomData:
    """
    A class to handle custom data input for prediction.
    
    This class takes student performance data and converts it into a format
    suitable for the machine learning model.
    """
    
    def __init__(self, gender: str, race_ethnicity: str, parental_level_of_education: str,
                 lunch: str, test_preparation_course: str, reading_score: int, writing_score: int):
        """
        Initialize CustomData with student information.
        
        Args:
            gender (str): Student's gender
            race_ethnicity (str): Student's race/ethnicity group
            parental_level_of_education (str): Parent's education level
            lunch (str): Type of lunch (standard/free/reduced)
            test_preparation_course (str): Whether test prep was completed
            reading_score (int): Reading test score (0-100)
            writing_score (int): Writing test score (0-100)
        """
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        """
        Convert the custom data into a pandas DataFrame.
        
        Returns:
            pd.DataFrame: DataFrame containing the input data
            
        Raises:
            CustomException: If DataFrame creation fails
        """
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

