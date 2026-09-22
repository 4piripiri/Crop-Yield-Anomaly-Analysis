# Crop Yield Anomaly Analysis

**Course:** Python Programming Laboratory — Capstone Project
**Problem Statement:** Identify unusually poor crop-yield years and determine whether rainfall, temperature, or other environmental factors contributed to the decline.
**Dataset:** [Indian Historical Crop Yield and Weather Data](https://www.kaggle.com/datasets/zoya77/indian-historical-crop-yield-and-weather-data/data) (Kaggle, zoya77)

## Project Structure

```
crop-yield-capstone/
├── data/
│   ├── raw/            # original Kaggle CSV(s) go here (gitignored)
│   └── processed/      # cleaned data saved here after running the pipeline
├── src/
│   ├── data_loader.py       # load raw data
│   ├── data_cleaning.py     # handle missing values, duplicates, outliers
│   ├── visualization.py     # matplotlib/seaborn charts
│   ├── stats_analysis.py    # anomaly detection + correlation/forecasting (scipy/statsmodels)
│   └── report_generator.py  # writes findings to outputs/reports
├── outputs/
│   ├── figures/         # saved charts
│   └── reports/         # final written report
├── main.py              # runs the full pipeline end-to-end
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Download the dataset from Kaggle and place the CSV(s) in `data/raw/`.

## Running

```bash
python main.py
```

## Team Split (suggested)

- **Person A** — `data_loader.py` + `data_cleaning.py` (Problem Definition, Data Cleaning criteria)
- **Person B** — `visualization.py` (Data Visualization criterion)
- **Person C** — `stats_analysis.py` (Statistical Analysis / Forecasting criterion)
- **Everyone** — `report_generator.py` + README + viva prep (Report Quality, Viva criteria)

## Rubric Coverage

| Criterion | Where it's addressed |
|---|---|
| Problem Definition & Dataset Selection | README + `data_loader.py` docstring |
| Code Structure & Modularity | `src/` package, one responsibility per module |
| Data Cleaning (NumPy/Pandas) | `data_cleaning.py` |
| Data Visualization (Matplotlib/Seaborn) | `visualization.py` |
| Statistical Analysis / Forecasting (SciPy/Statsmodels) | `stats_analysis.py` |
| Report Quality & Interpretation | `report_generator.py`, `outputs/reports/` |
