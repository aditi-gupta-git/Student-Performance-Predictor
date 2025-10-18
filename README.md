Student Exam Performance Predictor
=================================

Live demo: https://student-performance-predictor-0hqd.onrender.com

Predict a student's maths score from demographic factors and prior reading/writing scores using a trained ML pipeline, served via Flask.

Features
--------
- Flask web app with a simple form UI
- Sklearn preprocessing pipeline with numeric/categorical handling
- Model selection across multiple regressors with hyperparameter tuning
- Persisted preprocessor and model artifacts in `artifacts/`
- One-click deploy with Gunicorn + Procfile (compatible with Render/Heroku)

Tech stack
---------
- Python, Flask, Jinja2
- scikit-learn, CatBoost, XGBoost
- pandas, numpy

Project structure
-----------------
```text
.
├── app.py                      # Flask application
├── src/
│   ├── components/
│   │   ├── data_ingestion.py   # Load CSV, split train/test
│   │   ├── data_transformation.py # Preprocess pipelines, save preprocessor
│   │   └── model_trainer.py    # Model selection, tuning, save best model
│   ├── pipeline/
│   │   ├── predict_pipeline.py # Inference with saved artifacts
│   │   └── train_pipeline.py   # End-to-end training entrypoint
│   ├── utils.py                # IO helpers, grid search evaluate
│   ├── exception.py            # Custom exception wrapper
│   └── logger.py               # File logging setup
├── templates/                  # Jinja templates for UI
├── artifacts/                  # Saved data, preprocessor, model
├── notebook/                   # EDA and training notebooks
├── requirements.txt
├── setup.py
└── Procfile
```

Quick start
-----------
1) Setup environment
```bash
python -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

2) Train the model (artifacts will be created under `artifacts/`)
```bash
python -m src.pipeline.train_pipeline
```

3) Run locally
```bash
python app.py
# or production style
gunicorn app:app --bind 0.0.0.0:5000
```

4) Open the app
- Navigate to `http://127.0.0.1:5000/`

Usage
-----
- Fill in gender, race/ethnicity, parental education, lunch, test preparation, and prior reading/writing scores.
- Submit to get the predicted maths score. Artifacts must exist at `artifacts/model.pkl` and `artifacts/preprocessor.pkl`.

Data
----
- Training data is read from `notebook/data/stud.csv` inside the training pipeline.
- The pipeline splits into train/test and stores copies in `artifacts/train.csv` and `artifacts/test.csv`.

Deployment
----------
- The repository includes a `Procfile` for platforms like Render/Heroku. The command used is `gunicorn app:app`.

Development scripts
-------------------
Common commands:
```bash
# Run training
python -m src.pipeline.train_pipeline

# Start web server
python app.py

# Lint (once we add ruff/flake8)
ruff check .
```

Roadmap / Improvements
----------------------
- Add CI (GitHub Actions) to run formatting, linting, and a smoke test
- Add unit tests for `utils.load_object/save_object` and `PredictPipeline`
- Add type hints and docstrings for public functions
- Replace hardcoded paths with environment variables where appropriate
- Add Dockerfile for reproducible deployments
- Add CONTRIBUTING.md and CODE_OF_CONDUCT.md

License
-------
If you intend the project to be open-source, add a `LICENSE` file (e.g., MIT).
