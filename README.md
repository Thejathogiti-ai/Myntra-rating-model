# Myntra Rating Model — Full pipeline (Data inspection → Model → Deployment)

This repository contains an end-to-end pipeline that starts from a scraped Myntra product dataset, walks through exploratory analysis and feature engineering in a notebook, trains a model, serializes it, and exposes inference through a Streamlit app.

Quick summary:
- Dataset: myntra_dataset_ByScraping.xlsx (scraped product data)
- Notebook: Myntra-Logreg[Theja].ipynb (EDA, feature engineering, modelling)
- Model artifact: model.pkl (pickled trained model)
- Demo / deployment: app.py (Streamlit app)
- Dependencies: requirements.txt

---

## What this repo contains
- Myntra-Logreg[Theja].ipynb — exploratory data analysis, feature engineering, and model training cells (notebook is the canonical source for the analysis you performed).
- myntra_dataset_ByScraping.xlsx — dataset used by the notebook.
- model.pkl — serialized model used by the Streamlit app.
- app.py — Streamlit inference app that loads model.pkl and exposes a UI.
- requirements.txt — runtime dependencies.

---

## Data inspection (what was done)
Actions performed in the notebook (evidence from notebook cells):
- Loaded dataset from `myntra_dataset_ByScraping.xlsx`.
- Inspected data with df.head(), df.info(), df.describe(), df.isna().sum().
- Observed dataset size: ~52k rows and these columns: brand_name, pants_description, price, MRP, discount_percent, ratings, number_of_ratings (notebook also created a synthetic `sales` column and derived `revenue`).
- Examined value counts for categorical fields (e.g., brand counts — ~417 unique brands).
- Checked numeric ranges (price min/max, MRP ranges).
- Performed exploratory selection of top price/revenue records for further inspection.
- Created a price bucket function: `pricecategory` (Economical / Affordable / Premium / Luxury) for analysis.

Note: The notebook is the record of your EDA and contains the code cells that produced these checks and tables.

---

## Preprocessing & feature engineering (what you implemented)
Based on notebook contents and usage in the app:
- Added a synthetic `sales` column (np.random) for demonstration analysis.
- Computed `revenue = price * sales`.
- Defined a `pricecategory` function and applied price buckets for exploratory segmentation.
- Categorical fields used in modelling were represented by integer codes in the app: brand_name, pants_description, fashioncategory. Confirm whether the notebook encoded these or used a pipeline — see the notebook cells for exact encoding steps.

Important: The Streamlit app expects these categorical features as numeric codes at inference time. Ensure the same mapping/encoding used during training is applied at inference.

---

## Model training (what to reproduce)
Your notebook contains the modelling steps (the filename indicates logistic regression, but inspect the training cells to confirm the exact estimator and hyperparameters). To reproduce training from the notebook:

Option A — Re-run the notebook end-to-end (recommended if you want the original interactive workflow):
1. Open the notebook in Jupyter and run cells in order.
2. The notebook performs dataset loading, preprocessing, feature creation, model training and (apparently) produces a model.

Option B — Execute the notebook non-interactively:
```bash
pip install -r requirements.txt
jupyter nbconvert --to notebook --execute "Myntra-Logreg[Theja].ipynb" --inplace --ExecutePreprocessor.timeout=600
```
After successful execution the notebook will have the outputs; check where the model is serialized.

If you want a scriptable, reproducible training flow, extract the training cells into a `train.py` that:
- Loads the dataset
- Applies the same preprocessing/encoding
- Trains the estimator
- Evaluates on a validation set (accuracy/precision/recall/F1/ROC AUC)
- Serializes the final pipeline to `model.pkl` (preferably serializing a complete sklearn Pipeline that includes preprocessing)

Example to save model in Python:
```python
import pickle
with open("model.pkl", "wb") as f:
    pickle.dump(trained_pipeline_or_model, f)
```

---

## Model artifact (what exists)
- model.pkl is present at repository root and is loaded in `app.py` with pickle.
- The app expects the model to accept a pandas DataFrame with columns:
  ["brand_name", "pants_description", "fashioncategory", "price", "MRP", "discount_percent", "number_of_ratings"]

To inspect the pickled model object:
```python
import pickle
m = pickle.load(open("model.pkl","rb"))
print(type(m))
# If sklearn estimator/pipeline:
try:
    print(m.get_params())
except Exception:
    pass
```
This will tell you whether the pickled object contains preprocessing (transformers) or just the raw estimator.

---

## Inference / Streamlit app (deployed)
app.py:
- Loads model.pkl with pickle.
- Presents UI inputs:
  - price (number_input)
  - MRP (number_input)
  - Discount Percentage (number_input)
  - Number of Ratings (number_input)
  - Brand code (number_input)
  - Description code (number_input)
  - Fashion Category code (number_input)
- When the user clicks “predict”, the app constructs a single-row DataFrame with the columns listed above and calls `model.predict(data)`.
- App maps the returned label: 1 → "High Rated Product", 0 → "Low Rated Product".

Sample payload shape for inference (CSV-like):
brand_name,pants_description,fashioncategory,price,MRP,discount_percent,number_of_ratings
12,3,7,999.0,1299.0,23.1,350

Make sure categorical codes match the encoding used at training.

---

## How to run locally (from scratch to deployed demo)
1. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate    # Linux / macOS
.venv\Scripts\activate       # Windows
pip install --upgrade pip
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. (Optional) Reproduce training by executing the notebook (see “Model training” section).
4. Run the Streamlit app:
```bash
streamlit run app.py
```
5. The app will open in your browser; enter the input values and click predict.

---

## Minimal Dockerfile for deployment
If you want to containerize the demo (simple example):
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.enableCORS", "false"]
```
Build & run:
```bash
docker build -t myntra-rating-app .
docker run -p 8501:8501 myntra-rating-app
```

---

## Evaluation & checks you should confirm (recommended)
These are items to confirm or add to the notebook for completeness and reproducibility:
- Confirm the model algorithm and hyperparameters (logistic regression or otherwise) and record final evaluation metrics (accuracy, precision, recall, F1, ROC AUC) in the notebook or README.
- Confirm whether categorical encoding (brand/description/fashioncategory) is saved with the model or must be applied externally. If you used LabelEncoder / OrdinalEncoder / OneHotEncoder, include the encoder in the serialized pipeline.
- Check class balance for target variable and whether you used any sampling techniques.
- Add cross-validation and report mean ± std for metrics.
- Add a small unit test that loads model.pkl and runs a sanity prediction to ensure the app works after updates.

---

## Reproducibility suggestions (next steps)
- Extract the training cells into a `train.py` and save a reproducible artifact (sklearn Pipeline) that includes preprocessing and model.
- Save a JSON or pickle mapping file for categorical encodings (or include inside the pipeline).
- Add a `requirements.lock` or pinned requirements to avoid dependency drift.
- Add a simple test (e.g., tests/test_inference.py) that asserts the model produces expected shaped output for a canned input.
- Add a small GitHub Actions workflow to run tests on push.

---

## Contact
Repository owner: Thejathogiti-ai (GitHub)

---

## Closing notes
This README documents exactly what your repo currently contains and the sequence from initial data inspection (notebook) to a working Streamlit deployment. If you want, I can:
- update/commit this README.md to the repository for you, or
- extract the training cells into a reproducible `train.py` and create a pipeline that ensures the app and model remain consistent.

Which of the two would you like me to do next?