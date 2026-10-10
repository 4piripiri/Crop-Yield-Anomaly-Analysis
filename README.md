# Crop Yield Anomaly Analysis

**Course:** Python Programming Laboratory — Capstone Project
**Problem Statement:** Identify unusually poor crop-yield years and determine whether rainfall, temperature, or other environmental factors contributed to the decline.
**Dataset:** [Indian Historical Crop Yield and Weather Data](https://www.kaggle.com/datasets/zoya77/indian-historical-crop-yield-and-weather-data/data) (Kaggle, zoya77)

## Dataset Description

* **Size:** [N] records, [N] columns
* **Time span:** [start year] to [end year]
* **Coverage:** [N] states/districts and [N] crops
* **Target variable:** [yield column name] ([unit])
* **Environmental variables:** [rainfall column] ([unit]), [temperature column] ([unit]), [other columns, e.g. humidity, fertilizer, area]
* **Data quality notes:** [e.g. "X% missing values in column Y, handled in data_cleaning.py"]
* **Definition of "unusually poor":** a year whose yield z-score falls below [threshold, e.g. -1.5] relative to the mean.

## Project Structure

```text
crop-yield-capstone/
├── Custom_Crops_yield_Historical_Dataset.csv  # Raw data (gitignored)
├── cleaned_crop_data.csv                      # Cleaned data (gitignored)
├── data_cleaning.py                           # load data, handle missing values, duplicates
├── visualization.py                           # matplotlib/seaborn charts
├── stats_analysis.py                          # anomaly detection & correlation
├── report_generator.py                        # writes findings
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Download the dataset from Kaggle and place the raw CSV file (`Custom_Crops_yield_Historical_Dataset.csv`) directly into this main project folder.

## Running the Pipeline

Since we are using a flat script structure for clarity, run the modules individually in sequence:

```bash
python data_cleaning.py
python visualization.py
python stats_analysis.py
python report_generator.py
```


## Rubric Coverage

| Criterion | Where it's addressed |
| --- | --- |
| Problem Definition & Dataset Selection | README + `data_cleaning.py` initial outputs |
| Code Structure & Modularity | Flat modular structure, one responsibility per file |
| Data Cleaning (NumPy/Pandas) | `data_cleaning.py` |
| Data Visualization (Matplotlib/Seaborn) | `visualization.py` |
| Statistical Analysis / Forecasting (SciPy/Statsmodels) | `stats_analysis.py` |
| Report Quality & Interpretation | `report_generator.py` |
