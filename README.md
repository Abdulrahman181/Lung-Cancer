# Lung Cancer Classification (not a medical tool)

This repository contains an exploratory Jupyter notebook for a lung-cancer classification example. **It is not a diagnostic or screening tool** and must not be used to make health decisions. No clinical validation or model-performance claim is made here.

## Repository contents and data

The notebook is `Lung Cancer.ipynb`. It expects a local file named `data.csv` in the current working directory, but that dataset is **not included** in this repository. The notebook expects columns for the 15 input features and target used by its code: `GENDER`, `AGE`, `SMOKING`, `YELLOW_FINGERS`, `ANXIETY`, `PEER_PRESSURE`, `CHRONIC DISEASE`, `FATIGUE `, `ALLERGY `, `WHEEZING`, `ALCOHOL CONSUMING`, `COUGHING`, `SHORTNESS OF BREATH`, `SWALLOWING DIFFICULTY`, `CHEST PAIN`, and `LUNG_CANCER`. Some source column names contain spaces (including trailing spaces); match the actual file's headers before running.

Obtain any data independently and confirm its provenance, license, and suitability before use. Keep health data private: do not commit `data.csv`, patient-level outputs, credentials, or locally generated model files.

## Run locally

Use Python 3 with Jupyter and the notebook's imported libraries installed:

```bash
python -m pip install jupyter numpy pandas matplotlib seaborn scikit-learn xgboost
jupyter notebook "Lung Cancer.ipynb"
```

Run Jupyter from this repository directory after placing the authorized `data.csv` there. The notebook writes `lc.pkl` in the current directory if the final model-saving cell is run; do not load pickle files from untrusted sources. The checked-in notebook has its saved cell outputs cleared, so it will not display the prior run's tables, plots, or scores until you execute it locally.

## Limitations

The dataset is absent, so the notebook cannot be run end to end from this checkout and its previous reported scores are not reproducible here. Its train/test split, preprocessing, model selection, metrics, and example feature values have not been clinically or independently validated. Treat all output as an educational demonstration only.
