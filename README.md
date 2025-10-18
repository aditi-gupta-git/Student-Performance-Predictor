# 🎓 Student Performance Predictor

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Live Demo:** [https://student-performance-predictor-0hqd.onrender.com](https://student-performance-predictor-0hqd.onrender.com)

A full-stack machine learning web application that predicts student math scores based on various demographic and academic factors. Built with Flask, scikit-learn, and modern ML practices.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Architecture](#-project-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [Model Training](#-model-training)
- [Project Structure](#-project-structure)
- [API Endpoints](#-api-endpoints)
- [Dataset](#-dataset)
- [Model Performance](#-model-performance)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 Overview

This project predicts a student's **math score** based on:
- Gender
- Race/Ethnicity
- Parental level of education
- Lunch type (standard/free-reduced)
- Test preparation course completion
- Reading score
- Writing score

The system uses machine learning models trained on historical student performance data to provide accurate predictions, helping educators identify students who may need additional support.

---

## ✨ Features

- 🤖 **Multiple ML Models**: Compares 8 different regression models (Linear Regression, Random Forest, Gradient Boosting, XGBoost, CatBoost, AdaBoost, Decision Tree, K-Neighbors)
- 🎯 **Hyperparameter Tuning**: Automated GridSearchCV for optimal model selection
- 📊 **Data Pipeline**: Robust data ingestion, transformation, and preprocessing
- 🌐 **Web Interface**: Beautiful, responsive UI built with Tailwind CSS
- 📈 **Real-time Predictions**: Instant math score predictions via web form
- 🔄 **Automated Deployment**: Ready for deployment on Render, Heroku, or AWS
- 📝 **Logging & Error Handling**: Comprehensive logging and custom exception handling
- 🧪 **Model Persistence**: Saves trained models and preprocessors for efficient inference

---

## 🛠️ Tech Stack

### Backend
- **Python 3.8+**
- **Flask**: Web framework
- **scikit-learn**: ML models and preprocessing
- **XGBoost**: Gradient boosting
- **CatBoost**: Categorical boosting
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **dill**: Model serialization

### Frontend
- **HTML5/CSS3**
- **Tailwind CSS**: Styling
- **Jinja2**: Templating

### Deployment
- **Gunicorn**: WSGI HTTP Server
- **Render**: Cloud platform

---

## 🏗️ Project Architecture

```
┌─────────────────┐
│   Web Interface │
│    (Flask)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Predict Pipeline│
│  (predict.py)   │
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌─────────┐ ┌──────────────┐
│ Model   │ │ Preprocessor │
│ (.pkl)  │ │   (.pkl)     │
└─────────┘ └──────────────┘
```

### Training Pipeline

```
Data Ingestion → Data Transformation → Model Training → Model Evaluation → Model Persistence
```

1. **Data Ingestion** (`data_ingestion.py`): Loads and splits data
2. **Data Transformation** (`data_transformation.py`): 
   - Handles missing values
   - Scales numerical features (StandardScaler)
   - Encodes categorical features (OneHotEncoder)
3. **Model Training** (`model_trainer.py`):
   - Trains 8 different models
   - Performs GridSearchCV for hyperparameter tuning
   - Selects best model based on R² score
4. **Model Persistence**: Saves model and preprocessor as `.pkl` files

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/aditi-gupta-git/student-performance-predictor.git
   cd student-performance-predictor
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the project as a package** (optional)
   ```bash
   pip install -e .
   ```

---

## 🚀 Usage

### Running the Application Locally

1. **Start the Flask server**
   ```bash
   python app.py
   ```
   
   The application will automatically open in your browser at `http://127.0.0.1:5000/`

2. **Make predictions**
   - Navigate to the prediction page
   - Fill in the student details
   - Click "Predict Maths Score"
   - View the predicted score instantly

### Using the API

You can also make predictions programmatically:

```python
import requests

data = {
    'gender': 'female',
    'ethnicity': 'group B',
    'parental_level_of_education': "bachelor's degree",
    'lunch': 'standard',
    'test_preparation_course': 'completed',
    'reading_score': 72,
    'writing_score': 74
}

response = requests.post('http://127.0.0.1:5000/predictdata', data=data)
print(response.text)
```

---

## 🧪 Model Training

To retrain the models with new data:

1. **Place your dataset** at `notebook/data/stud.csv`

2. **Run the training pipeline**
   ```bash
   python src/components/data_ingestion.py
   ```

This will:
- Ingest the data
- Perform train-test split (80-20)
- Transform features
- Train and evaluate 8 models
- Save the best model and preprocessor to `artifacts/`

### Tested Models

The system evaluates the following models:
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- AdaBoost Regressor
- K-Neighbors Regressor
- XGBoost Regressor
- CatBoost Regressor

---

## 📁 Project Structure

```
student-performance-predictor/
│
├── app.py                          # Flask application entry point
├── setup.py                        # Package setup configuration
├── requirements.txt                # Python dependencies
├── Procfile                        # Deployment configuration
├── LICENSE                         # MIT License
├── README.md                       # Project documentation
│
├── src/                            # Source code
│   ├── __init__.py
│   ├── logger.py                   # Logging configuration
│   ├── exception.py                # Custom exception handling
│   ├── utils.py                    # Utility functions
│   │
│   ├── components/                 # ML pipeline components
│   │   ├── __init__.py
│   │   ├── data_ingestion.py      # Data loading and splitting
│   │   ├── data_transformation.py  # Feature engineering
│   │   └── model_trainer.py        # Model training and evaluation
│   │
│   └── pipeline/                   # Prediction pipeline
│       ├── predict_pipeline.py     # Inference pipeline
│       └── train_pipeline.py       # Training pipeline
│
├── templates/                      # HTML templates
│   ├── base.html                   # Base template
│   ├── index.html                  # Landing page
│   └── home.html                   # Prediction form
│
├── artifacts/                      # Generated artifacts
│   ├── model.pkl                   # Trained model
│   ├── preprocessor.pkl            # Data preprocessor
│   ├── train.csv                   # Training data
│   ├── test.csv                    # Test data
│   └── data.csv                    # Raw data
│
├── notebook/                       # Jupyter notebooks
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb
│   ├── 2. MODEL TRAINING.ipynb
│   └── data/
│       └── stud.csv                # Original dataset
│
└── logs/                           # Application logs
```

---

## 🌐 API Endpoints

### `GET /`
Returns the landing page with project overview and statistics.

### `GET /predictdata`
Returns the prediction form page.

### `POST /predictdata`
Accepts form data and returns the predicted math score.

**Request Body:**
```json
{
  "gender": "female",
  "ethnicity": "group B",
  "parental_level_of_education": "bachelor's degree",
  "lunch": "standard",
  "test_preparation_course": "completed",
  "reading_score": 72,
  "writing_score": 74
}
```

**Response:**
Returns HTML page with the predicted score displayed.

---

## 📊 Dataset

The project uses the **Students Performance in Exams** dataset, which contains:

- **1000 rows** of student data
- **8 columns**: 
  - `gender`: Male/Female
  - `race_ethnicity`: Group A/B/C/D/E
  - `parental_level_of_education`: Various education levels
  - `lunch`: Standard or free/reduced
  - `test_preparation_course`: Completed or none
  - `math_score`: Target variable (0-100)
  - `reading_score`: Feature (0-100)
  - `writing_score`: Feature (0-100)

**Data Source**: The dataset is commonly used for educational ML projects and is available in `notebook/data/stud.csv`.

---

## 📈 Model Performance

The system automatically selects the best-performing model based on R² score. Typical performance metrics:

| Model | R² Score (Test) | Training Time |
|-------|----------------|---------------|
| **Linear Regression** | ~0.85 | Very Fast |
| **Random Forest** | ~0.88 | Medium |
| **Gradient Boosting** | ~0.89 | Medium-Slow |
| **XGBoost** | ~0.88 | Medium |
| **CatBoost** | ~0.88 | Medium |

*Note: Actual performance may vary based on hyperparameter tuning and data split.*

The model achieves:
- ✅ **R² Score > 0.85**: Strong predictive performance
- ✅ **Low prediction latency**: < 100ms per prediction
- ✅ **Robust to outliers**: Through proper preprocessing

---

## 🚢 Deployment

### Deploying to Render

1. **Fork this repository**

2. **Create a new Web Service** on [Render](https://render.com/)

3. **Configure the service:**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: Python 3

4. **Deploy**: Render will automatically deploy your app

### Deploying to Heroku

```bash
# Login to Heroku
heroku login

# Create a new app
heroku create your-app-name

# Push to Heroku
git push heroku main

# Open the app
heroku open
```

### Local Production Server

```bash
gunicorn --bind 0.0.0.0:8000 app:app
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Ideas for Contributions
- Add more sophisticated models (Neural Networks, Ensemble methods)
- Implement model explainability (SHAP, LIME)
- Add unit tests
- Improve UI/UX
- Add data visualization dashboards
- Implement A/B testing for models

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👤 Contact

**Aditi Gupta**

- LinkedIn: [linkedin.com/in/guptaaditi8](https://www.linkedin.com/in/guptaaditi8)
- GitHub: [github.com/aditi-gupta-git](https://github.com/aditi-gupta-git)
- Email: guptaaditi.0825@gmail.com

---

## 🙏 Acknowledgments

- Dataset inspired by educational performance research
- Built with guidance from modern MLOps practices
- UI design inspired by modern web design trends

---

## 📸 Screenshots

### Landing Page
Modern, responsive landing page with project overview and statistics.

### Prediction Form
Intuitive form to input student details and get instant predictions.

### Results
Clear display of predicted math scores with contextual information.

---

## 🔮 Future Enhancements

- [ ] Add authentication and user profiles
- [ ] Implement model versioning and A/B testing
- [ ] Add real-time model monitoring and drift detection
- [ ] Create REST API with FastAPI
- [ ] Add data visualization dashboard
- [ ] Implement batch prediction capabilities
- [ ] Add model explainability features
- [ ] Support multiple languages
- [ ] Add mobile app support
- [ ] Integrate with learning management systems

---

<div align="center">
  
**⭐ Star this repository if you find it helpful!**

Made with ❤️ by [Aditi Gupta](https://github.com/aditi-gupta-git)

</div>
