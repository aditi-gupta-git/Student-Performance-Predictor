# 🎓 Student Performance Predictor

A machine learning web application that predicts student math scores based on various demographic and academic factors. Built with Flask, scikit-learn, and deployed on Render.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Online-brightgreen)](https://student-performance-predictor-0hqd.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.9+-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🌟 Features

- **Real-time Predictions**: Get instant math score predictions based on student data
- **Interactive Web Interface**: Clean, responsive UI built with HTML/CSS/JavaScript
- **Input Validation**: Comprehensive form validation with error handling
- **Multiple ML Models**: Supports various algorithms (CatBoost, XGBoost, Random Forest, etc.)
- **Docker Support**: Easy deployment with Docker and Docker Compose
- **Comprehensive Logging**: Detailed logging for monitoring and debugging
- **Unit Tests**: Test coverage for core functionality

## 🚀 Live Demo

Try the application at: [https://student-performance-predictor-0hqd.onrender.com](https://student-performance-predictor-0hqd.onrender.com)

## 📊 Dataset

The model is trained on a dataset containing 1000 student records with the following features:

- **Gender**: Male/Female
- **Race/Ethnicity**: Group A, B, C, D, E
- **Parental Level of Education**: Various education levels
- **Lunch Type**: Standard/Free or Reduced
- **Test Preparation Course**: None/Completed
- **Reading Score**: 0-100
- **Writing Score**: 0-100
- **Math Score**: 0-100 (target variable)

Dataset source: [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

## 🛠️ Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/student-performance-predictor.git
   cd student-performance-predictor
   ```

2. **Create a virtual environment**
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

### Docker Installation

1. **Using Docker Compose (Recommended)**
   ```bash
   docker-compose up --build
   ```

2. **Using Docker directly**
   ```bash
   docker build -t student-performance-predictor .
   docker run -p 5000:5000 student-performance-predictor
   ```

## 📁 Project Structure

```
student-performance-predictor/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── setup.py                       # Package setup configuration
├── Procfile                       # Heroku deployment configuration
├── Dockerfile                     # Docker configuration
├── docker-compose.yml             # Docker Compose configuration
├── README.md                      # Project documentation
├── src/                           # Source code
│   ├── __init__.py
│   ├── exception.py               # Custom exception handling
│   ├── logger.py                  # Logging configuration
│   ├── utils.py                   # Utility functions
│   ├── components/                # ML pipeline components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   └── pipeline/                  # Training and prediction pipelines
│       ├── train_pipeline.py
│       └── predict_pipeline.py
├── templates/                     # HTML templates
│   ├── base.html
│   ├── index.html
│   └── home.html
├── artifacts/                     # Trained models and preprocessors
│   ├── model.pkl
│   ├── preprocessor.pkl
│   └── data.csv
├── notebook/                      # Jupyter notebooks for EDA and training
│   ├── 1 . EDA STUDENT PERFORMANCE .ipynb
│   └── 2. MODEL TRAINING.ipynb
├── tests/                         # Unit tests
│   ├── __init__.py
│   └── test_predict_pipeline.py
└── catboost_info/                 # CatBoost training logs
```

## 🧪 Usage

### Web Interface

1. Open the application in your browser
2. Fill in the student information form:
   - Select gender and ethnicity
   - Choose parental education level
   - Select lunch type and test preparation status
   - Enter reading and writing scores (0-100)
3. Click "Predict Maths Score" to get the prediction
4. View the predicted math score and try different scenarios

### API Usage

The application also supports programmatic access:

```python
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Create input data
data = CustomData(
    gender="female",
    race_ethnicity="group A",
    parental_level_of_education="bachelor's degree",
    lunch="standard",
    test_preparation_course="completed",
    reading_score=85,
    writing_score=90
)

# Get prediction
df = data.get_data_as_data_frame()
pipeline = PredictPipeline()
prediction = pipeline.predict(df)
print(f"Predicted math score: {prediction[0]}")
```

## 🧪 Testing

Run the unit tests to verify the application functionality:

```bash
python -m pytest tests/ -v
```

Or run specific test files:

```bash
python tests/test_predict_pipeline.py
```

## 📈 Model Performance

The model uses various machine learning algorithms and selects the best performing one:

- **CatBoost Regressor**: Primary model
- **XGBoost Regressor**: Alternative model
- **Random Forest Regressor**: Ensemble method
- **Linear Regression**: Baseline model

Performance metrics are logged during training and can be viewed in the training notebooks.

## 🚀 Deployment

### Render Deployment

1. Connect your GitHub repository to Render
2. Set the build command: `pip install -r requirements.txt`
3. Set the start command: `gunicorn app:app`
4. Deploy!

### Heroku Deployment

1. Install Heroku CLI
2. Login to Heroku: `heroku login`
3. Create app: `heroku create your-app-name`
4. Deploy: `git push heroku main`

### Docker Deployment

1. Build image: `docker build -t student-performance-predictor .`
2. Run container: `docker run -p 5000:5000 student-performance-predictor`

## 🔧 Configuration

### Environment Variables

- `FLASK_ENV`: Set to `production` for production deployment
- `PORT`: Port number (default: 5000)

### Logging

Logs are written to `app.log` and console. Log levels can be configured in `app.py`.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests for new functionality
5. Commit your changes: `git commit -m "Add feature"`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Aditi Gupta**
- Email: guptaaditi.0825@gmail.com
- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- Dataset provided by [Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- Flask framework for web development
- scikit-learn for machine learning tools
- Render for hosting the application

## 📊 Future Enhancements

- [ ] Add more sophisticated feature engineering
- [ ] Implement model versioning
- [ ] Add confidence intervals to predictions
- [ ] Create admin dashboard for model monitoring
- [ ] Add data visualization features
- [ ] Implement user authentication
- [ ] Add batch prediction API
- [ ] Create mobile app version

## 🐛 Known Issues

- Model files need to be present in the `artifacts/` directory
- Some browsers may cache old versions of the application

## 📞 Support

If you encounter any issues or have questions, please:

1. Check the [Issues](https://github.com/yourusername/student-performance-predictor/issues) page
2. Create a new issue with detailed information
3. Contact the author via email

---

⭐ If you found this project helpful, please give it a star!