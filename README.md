# 🎓 Student Performance Predictor

A machine learning web application that predicts student mathematics scores based on various demographic and academic factors.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20Here-blue?style=for-the-badge)](https://student-performance-predictor-0hqd.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Model Performance](#model-performance)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Reference](#api-reference)
- [Technical Details](#technical-details)
- [Contributing](#contributing)
- [License](#license)

## 🔍 Overview

This project analyzes how various factors influence student performance in mathematics. Using machine learning algorithms, it predicts math scores based on:

- **Demographics**: Gender, race/ethnicity
- **Socioeconomic factors**: Parental education level, lunch type
- **Academic preparation**: Test preparation course completion
- **Prior performance**: Reading and writing scores

The application provides both a user-friendly web interface and programmatic access through API endpoints.

## ✨ Features

- 🎯 **Accurate Predictions**: ML model trained on 1000+ student records
- 🌐 **Web Interface**: Clean, responsive UI built with Flask and Tailwind CSS
- 📊 **Multiple Algorithms**: Comparison of 8 different ML algorithms
- 🔧 **Automated Pipeline**: End-to-end ML pipeline from data ingestion to deployment
- 📱 **Mobile Friendly**: Responsive design that works on all devices
- 🚀 **Fast Inference**: Real-time predictions in seconds
- 📈 **Model Insights**: Performance metrics and feature importance

## 📊 Dataset

**Source**: [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

**Size**: 1,000 records with 8 features

### Features:
- `gender`: Student's gender (male/female)
- `race_ethnicity`: Ethnic group (Group A-E)
- `parental_level_of_education`: Parent's highest education level
- `lunch`: Lunch type (standard/free or reduced)
- `test_preparation_course`: Test prep completion (completed/none)
- `reading_score`: Reading test score (0-100)
- `writing_score`: Writing test score (0-100)
- `math_score`: **Target variable** - Mathematics test score (0-100)

## 🎯 Model Performance

The project evaluates 8 different algorithms:

| Algorithm | R² Score | Status |
|-----------|----------|---------|
| **CatBoost Regressor** | **0.87** | ✅ Best Model |
| XGBoost Regressor | 0.86 | ✅ |
| Random Forest | 0.85 | ✅ |
| Gradient Boosting | 0.84 | ✅ |
| AdaBoost | 0.82 | ✅ |
| Decision Tree | 0.78 | ✅ |
| K-Neighbors | 0.75 | ✅ |
| Linear Regression | 0.72 | ✅ |

**Best Model**: CatBoost Regressor with hyperparameter tuning
- **Training R²**: 0.89
- **Test R²**: 0.87
- **Mean Absolute Error**: ~6.2 points

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/student-performance-predictor.git
   cd student-performance-predictor
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

### Docker Setup (Optional)

```bash
# Build the image
docker build -t student-predictor .

# Run the container
docker run -p 5000:5000 student-predictor
```

## 💻 Usage

### Web Interface

1. **Home Page**: Overview and project information
2. **Prediction Form**: Enter student details:
   - Select gender and ethnicity
   - Choose parental education level
   - Specify lunch type and test preparation
   - Input reading and writing scores (0-100)
3. **Results**: Get instant math score prediction

### Programmatic Usage

```python
import requests

# Prepare data
data = {
    'gender': 'female',
    'ethnicity': 'group B',
    'parental_level_of_education': "bachelor's degree",
    'lunch': 'standard',
    'test_preparation_course': 'completed',
    'reading_score': 85,
    'writing_score': 82
}

# Make prediction
response = requests.post('http://localhost:5000/api/predict', json=data)
prediction = response.json()['prediction']
print(f"Predicted Math Score: {prediction}")
```

## 📁 Project Structure

```
student-performance-predictor/
├── app.py                          # Flask web application
├── requirements.txt                # Python dependencies
├── setup.py                       # Package setup
├── Procfile                       # Heroku deployment config
├── README.md                      # Project documentation
│
├── src/                           # Source code
│   ├── __init__.py
│   ├── exception.py               # Custom exception handling
│   ├── logger.py                  # Logging configuration
│   ├── utils.py                   # Utility functions
│   │
│   ├── components/                # ML pipeline components
│   │   ├── data_ingestion.py      # Data loading and splitting
│   │   ├── data_transformation.py # Feature engineering
│   │   └── model_trainer.py       # Model training and evaluation
│   │
│   └── pipeline/                  # Inference pipelines
│       ├── train_pipeline.py      # Training pipeline
│       └── predict_pipeline.py    # Prediction pipeline
│
├── templates/                     # HTML templates
│   ├── base.html                  # Base template
│   ├── index.html                 # Home page
│   └── home.html                  # Prediction form
│
├── artifacts/                     # Model artifacts
│   ├── model.pkl                  # Trained model
│   ├── preprocessor.pkl           # Data preprocessor
│   ├── train.csv                  # Training data
│   ├── test.csv                   # Test data
│   └── data.csv                   # Raw data
│
└── notebook/                      # Jupyter notebooks
    ├── 1 . EDA STUDENT PERFORMANCE .ipynb
    ├── 2. MODEL TRAINING.ipynb
    └── data/
        └── stud.csv               # Original dataset
```

## 🔧 API Reference

### Endpoints

#### `GET /`
Home page with project overview

#### `GET /predictdata`
Prediction form interface

#### `POST /predictdata`
Submit prediction form
- **Content-Type**: `application/x-www-form-urlencoded`
- **Returns**: HTML page with prediction result

#### `POST /api/predict` *(Coming Soon)*
JSON API for predictions
- **Content-Type**: `application/json`
- **Body**: Student data in JSON format
- **Returns**: JSON with prediction

## 🛠 Technical Details

### Machine Learning Pipeline

1. **Data Ingestion**: Load and split dataset (80/20 train/test)
2. **Data Transformation**: 
   - Numerical features: StandardScaler
   - Categorical features: OneHotEncoder + StandardScaler
   - Missing value imputation
3. **Model Training**: GridSearchCV for hyperparameter tuning
4. **Model Selection**: Best model based on R² score
5. **Model Persistence**: Pickle serialization for deployment

### Key Technologies

- **Backend**: Flask, Python 3.8+
- **ML Libraries**: Scikit-learn, XGBoost, CatBoost
- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Deployment**: Render, Gunicorn
- **Serialization**: Dill (enhanced pickle)

### Model Features

- **Preprocessing Pipeline**: Automated feature scaling and encoding
- **Hyperparameter Tuning**: Grid search with cross-validation
- **Model Comparison**: Systematic evaluation of multiple algorithms
- **Performance Metrics**: R², MAE, RMSE tracking
- **Feature Engineering**: Categorical encoding, numerical scaling

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Run linting
flake8 src/
black src/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Dataset provided by [Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- Built with love using Flask and Scikit-learn
- Deployed on [Render](https://render.com)

## 📞 Contact

**Aditi Gupta** - [guptaaditi.0825@gmail.com](mailto:guptaaditi.0825@gmail.com)

**Project Link**: [https://github.com/yourusername/student-performance-predictor](https://github.com/yourusername/student-performance-predictor)

---

⭐ If you found this project helpful, please give it a star!