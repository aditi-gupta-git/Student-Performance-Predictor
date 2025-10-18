# Student Exam Performance Predictor

Live demo: https://student-performance-predictor-0hqd.onrender.com

Predict a student's Maths score from demographics and prior scores using a trained ML pipeline. This project includes a Flask web app for inference, a modular training pipeline, and ready-to-deploy configuration.

## Features
- Web UI built with Flask and Tailwind (Jinja templates)
- Predicts Maths score from:
  - gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course
  - reading_score, writing_score
- ML pipeline with preprocessing (imputation, one-hot encoding, scaling) and model selection
- Trained artifacts bundled in `artifacts/` (`model.pkl`, `preprocessor.pkl`)
- Clear module structure for data ingestion, transformation, training, and inference
- Production-ready `Procfile` (gunicorn) for platforms like Render/Heroku
- Logging and custom exception handling

## Tech stack
- Python, Flask, Jinja, Tailwind CDN
- scikit-learn, CatBoost, XGBoost, NumPy, Pandas
- gunicorn for production serving

## Project structure
```text
.
├─ app.py                      # Flask app (web UI + inference route)
├─ Procfile                   # gunicorn entry for production
├─ requirements.txt           # runtime dependencies
├─ setup.py                   # install helper (optional)
├─ artifacts/                 # trained artifacts (model + preprocessor)
├─ notebook/                  # EDA and training notebooks + raw data
├─ src/
│  ├─ components/
│  │  ├─ data_ingestion.py
│  │  ├─ data_transformation.py
│  │  └─ model_trainer.py
│  ├─ pipeline/
│  │  ├─ predict_pipeline.py  # loads artifacts and runs inference
│  │  └─ train_pipeline.py    # orchestrates training (CLI entry)
│  ├─ exception.py
│  ├─ logger.py
│  └─ utils.py
└─ templates/                 # Jinja templates (Tailwind UI)
   ├─ base.html
   ├─ home.html
   └─ index.html
```

## Quickstart (local)
- Prerequisites: Python 3.9–3.11 recommended

```bash
# 1) Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 3) Run the app (development)
python app.py
# The app will open a browser tab at http://127.0.0.1:5000/
```

For production serving locally (optional):
```bash
gunicorn app:app --bind 0.0.0.0:8000 --workers 2
```

## Re-train the model
Artifacts are provided in `artifacts/` so inference works out-of-the-box. To regenerate them:
```bash
python -m src.pipeline.train_pipeline
```
This will:
- Ingest data from `notebook/data/stud.csv`
- Split into train/test and save CSVs to `artifacts/`
- Fit preprocessing, run model selection, save `preprocessor.pkl` and `model.pkl` to `artifacts/`

## Usage (Web UI)
- Home: provides overview and CTA
- Predict: fill out the form and submit to get a Maths score prediction immediately

## API (form POST)
Endpoint: `POST /predictdata`

Form fields:
- `gender`: `male` | `female`
- `ethnicity`: `group A`|`group B`|`group C`|`group D`|`group E`
- `parental_level_of_education`: one of ["associate's degree","bachelor's degree","high school","master's degree","some college","some high school"]
- `lunch`: `free/reduced` | `standard`
- `test_preparation_course`: `none` | `completed`
- `reading_score`: 0–100
- `writing_score`: 0–100

Example cURL:
```bash
curl -X POST http://127.0.0.1:5000/predictdata \
  -F gender=female \
  -F ethnicity="group B" \
  -F parental_level_of_education="bachelor's degree" \
  -F lunch=standard \
  -F test_preparation_course=completed \
  -F reading_score=88 \
  -F writing_score=91
```

## Deployment
This repo is ready to deploy to Render/Heroku using the `Procfile`:
- Web command: `gunicorn app:app`
- Ensure Python version is supported (3.9–3.11). On Render, select a Python environment and set the Start Command to the above
- The app binds to `$PORT` automatically when run via gunicorn

## Notes
- The training pipeline evaluates multiple regressors (Random Forest, Gradient Boosting, CatBoost, XGBoost, etc.) and selects the best by validation R², persisting the fitted model
- Preprocessing includes imputing, one-hot encoding of categoricals, and scaling numerics
- Logs are written to `./logs/`

## Acknowledgements
- Dataset from common student performance datasets used in EDA tutorials
- Thanks to scikit-learn, CatBoost, and XGBoost communities for tooling
