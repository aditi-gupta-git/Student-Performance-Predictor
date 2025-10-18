from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import threading
import webbrowser
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")


from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        try:
            # Validate required fields
            required_fields = ['gender', 'ethnicity', 'parental_level_of_education', 
                             'lunch', 'test_preparation_course', 'reading_score', 'writing_score']
            
            for field in required_fields:
                if not request.form.get(field):
                    return render_template('home.html', error=f"Please provide {field.replace('_', ' ')}")
            
            # Validate score ranges
            try:
                reading_score = float(request.form.get('reading_score'))
                writing_score = float(request.form.get('writing_score'))
                
                if not (0 <= reading_score <= 100):
                    return render_template('home.html', error="Reading score must be between 0 and 100")
                if not (0 <= writing_score <= 100):
                    return render_template('home.html', error="Writing score must be between 0 and 100")
                    
            except ValueError:
                return render_template('home.html', error="Scores must be valid numbers")
            
            # Create data object
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=reading_score,
                writing_score=writing_score
            )
            
            pred_df = data.get_data_as_data_frame()
            
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            
            # Round result to 1 decimal place
            prediction = round(float(results[0]), 1)
            
            return render_template('home.html', results=prediction)
            
        except Exception as e:
            return render_template('home.html', error=f"An error occurred during prediction: {str(e)}")
           

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__=="__main__":
    threading.Timer(1.5, open_browser).start()
    app.run(host="0.0.0.0", port=5000, debug=True)
