# Engineering Review — Lung-Cancer

## Scope and baseline

- Repository audited: `Abdulrahman181/Lung-Cancer` only.
- Baseline contained one notebook, `Lung Cancer.ipynb`; there were no Python modules, README, requirements file, tests, or committed dataset.
- The notebook referenced `data.csv`, but that file is not present in the repository. No data, model artifact, or performance metric was fabricated.

## Findings and fixes

### Critical / blocking

1. **Missing dataset** — the original first data cell assumed `data.csv` existed and failed unclearly depending on the working directory. The notebook now resolves `LUNG_CANCER_DATA` or `data.csv` and raises an actionable `FileNotFoundError` before training when absent.
2. **Weak reproducibility and split design** — the original split was unstratified and only seeded once. The revised notebook uses a fixed seed and stratified 80/20 split, then performs seeded 5-fold stratified CV on the training partition only.
3. **Test-set model selection risk** — the original notebook printed several test-set scores without a selection protocol. The revised flow selects the model by training-fold CV F1, refits that model on training rows, and evaluates the untouched test partition once.
4. **Unstable/partial metrics** — the original flow primarily reported accuracy and reused a mutable `y_pred` for plotting. The revised flow computes accuracy, balanced accuracy, precision, recall, F1, ROC-AUC when probabilities are available, a classification report, and a held-out confusion matrix from explicit variables.
5. **Implicit schema and encoding assumptions** — the original code depended on positional columns and trailing spaces such as `FATIGUE `. The revised flow normalizes column names, validates the complete named schema, validates `M/F` and `YES/NO`, rejects missing/unknown/non-finite values, and uses named feature columns.
6. **Heavy undeclared dependency** — the original notebook imported XGBoost without a requirements file. XGBoost was removed from the baseline candidate set in favor of declared scikit-learn estimators; dependencies are now explicit and installable.

### Quality and safety

- Removed arbitrary hard-coded sample prediction input; `predict_one` now requires caller-provided feature values matching the validated schema.
- Removed stale notebook outputs, execution counts, and the original exploratory state.
- Model preprocessing (standardization for logistic regression/KNN) is inside pipelines, so scaling is fit within each CV fold and cannot leak test information.
- Artifacts are written only after a successful data-backed run to `artifacts/lc.pkl`, which is ignored by Git.
- Added a standard-library static validator that parses every notebook code cell with AST, rejects stale outputs/counts, flags local absolute path markers, and checks for the data-missing guard.

## Validation performed

- `python3 validate_repo.py` — passed.
- `python3 -m unittest discover -s tests -v` — 3 tests passed.
- `python3 -m compileall -q validate_repo.py tests` — passed.
- `ruff check validate_repo.py tests` — passed (Ruff was available).
- `git diff --check` — passed.
- Notebook inspection confirms 17 cells, zero saved outputs, and zero execution counts.

## Not run / limitations

A full notebook execution and trustworthy ML metric run were **not performed** because the repository does not contain `data.csv` and no authorized replacement dataset was supplied. Installing or exercising the full ML stack was not used to manufacture a result. Once the real dataset is supplied, execute the documented notebook command and review the resulting metrics for domain appropriateness.
