# Lung Cancer Classification

This repository contains a reproducible scikit-learn notebook for binary lung-cancer classification from tabular risk-factor data.

## Data contract

The notebook expects a CSV file at `data.csv` by default. Set `LUNG_CANCER_DATA` to use another path. The file must contain these columns (column names are normalized by trimming whitespace and replacing spaces with underscores):

- `GENDER`, `AGE`, `SMOKING`, `YELLOW_FINGERS`, `ANXIETY`, `PEER_PRESSURE`, `CHRONIC_DISEASE`
- `FATIGUE`, `ALLERGY`, `WHEEZING`, `ALCOHOL_CONSUMING`, `COUGHING`, `SHORTNESS_OF_BREATH`
- `SWALLOWING_DIFFICULTY`, `CHEST_PAIN`, and target `LUNG_CANCER`

`GENDER` must contain `M`/`F` and `LUNG_CANCER` must contain `YES`/`NO`. Missing values and unknown categorical values are rejected rather than silently imputed or fabricated.

The dataset is intentionally **not committed**. If it is absent, execution stops with an actionable `FileNotFoundError`; no metrics or sample predictions are invented.

## Setup and use

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
# Put the authorized dataset at data.csv, or set LUNG_CANCER_DATA=/path/to/data.csv
jupyter nbconvert --execute --to notebook --inplace "Lung Cancer.ipynb"
```

The notebook creates `artifacts/lc.pkl` only after successful training. It uses a stratified, seeded hold-out test set. Model selection is performed by seeded stratified cross-validation on the training partition; the test partition is evaluated once at the end. Reported metrics are therefore only available when the real dataset is supplied.

## Validation

Run the repository checks without data or heavyweight ML execution:

```bash
python validate_repo.py
python -m unittest discover -s tests -v
```

These checks parse every notebook code cell with Python AST, reject stale notebook outputs and execution counts, and flag local absolute paths. They do not claim a completed training run.
