# 🌾 Crop Yield Anomaly Analysis

### Identifying Unusual Agricultural Yield Patterns Using Statistical Analysis and Python

## 📌 Project Overview

Crop Yield Anomaly Analysis is a Python-based data analytics project that identifies unusually poor crop-yield years using historical Indian agricultural data.

The project focuses on **Rice**, one of India's major staple crops, to investigate historical yield fluctuations and examine their relationship with environmental factors such as rainfall and temperature.

Using data preprocessing, statistical analysis, visualization and time-series forecasting, the project aims to identify unusual yield patterns and generate meaningful insights from historical agricultural data.

## 🎯 Problem Statement

Agricultural crop yields fluctuate over time due to environmental conditions and other agricultural factors.

Unusually low crop yields can affect farmers' income, food availability and agricultural planning.

This project addresses the following questions:

* Which years experienced unusually low rice yields?
* How did actual yield compare with the expected historical trend?
* Is there a statistical relationship between yield fluctuations and rainfall or temperature?
* Can historical yield patterns be used to forecast future crop yields?

## 🎯 Project Objectives

1. Clean and preprocess historical agricultural data.
2. Analyse annual rice-yield trends.
3. Identify unusually poor-yield years using Z-score-based anomaly detection.
4. Examine relationships between yield fluctuations, rainfall and temperature.
5. Apply statistical hypothesis testing to compare environmental conditions.
6. Perform time-series analysis and forecast future crop yields.

## 🌾 Why Rice?

Rice was selected because:

* It is one of India's major staple food crops.
* It plays an important role in national food security.
* Its cultivation is influenced by rainfall, temperature and water availability.
* Historical rice-yield data provides an opportunity to study agricultural fluctuations.

Focusing on one crop allows a more specific analysis without combining crops with different growing requirements.

## 📊 Dataset Description

**Dataset:** Indian Historical Crop Yield and Weather Data

**Source:** Kaggle — zoya77

The dataset contains historical agricultural observations and environmental variables.

### Important Features

| Feature         | Description                             |
| --------------- | --------------------------------------- |
| Year            | Year of agricultural observation        |
| Crop            | Name of the crop                        |
| Yield_kg_per_ha | Crop yield in kilograms per hectare     |
| Rainfall_mm     | Rainfall measured in millimetres        |
| Temperature_C   | Temperature measured in degrees Celsius |
| Area_ha         | Agricultural area in hectares           |

The project filters the dataset to analyse Rice.

## ⚙️ Project Methodology

The project follows three major stages.

### 1. Data Cleaning and Preprocessing

File: `data_cleaning.py`

Pandas is used to:

* Remove duplicate records.
* Handle missing values.
* Remove unnecessary spaces from categorical values.
* Handle invalid numerical observations.
* Validate agricultural area and yield values.
* Generate a cleaned CSV dataset.

**Output:** `cleaned_crop_data.csv`

### 2. Data Visualization

File: `visualization.py`

Matplotlib and Seaborn are used to explore agricultural patterns through graphs.

The visualizations include:

* Annual crop-yield trends.
* Poor-yield year comparisons.
* Rainfall and crop-yield relationships.
* Temperature and crop-yield relationships.

These graphs help identify patterns and understand changes in agricultural productivity.

### 3. Statistical Analysis

File: `stats_analysis.py`

The project applies multiple statistical techniques.

| Technique              | Purpose                                                              |
| ---------------------- | -------------------------------------------------------------------- |
| Descriptive Statistics | Summarizes the dataset                                               |
| Linear Regression      | Identifies the overall yield trend                                   |
| Z-score                | Detects unusually poor-yield years                                   |
| Shapiro-Wilk Test      | Checks normality of yield deviations                                 |
| Pearson Correlation    | Examines linear relationships between yield gaps and weather         |
| Independent T-test     | Compares weather conditions in poor and normal years                 |
| Mann-Whitney U Test    | Provides a non-parametric group comparison                           |
| One-sample T-test      | Compares poor-year yield with overall average yield                  |
| Paired T-test          | Compares rainfall in poor-yield years with preceding years           |
| ANOVA                  | Compares yield gaps across rainfall categories                       |
| Kruskal-Wallis Test    | Performs non-parametric group comparison                             |
| Chi-square Test        | Examines associations between anomaly status and rainfall categories |
| OLS Regression         | Models the relationship between yield gaps and weather variables     |
| Moving Average         | Smooths short-term yield fluctuations                                |
| ADF Test               | Checks time-series stationarity                                      |
| ARIMA                  | Forecasts future crop yield                                          |

## 🔍 Anomaly Detection Methodology

The project uses a trend-based Z-score approach.

**Step 1: Calculate the historical yield trend**

Linear regression is applied to estimate the expected yield over time.

**Step 2: Calculate the yield gap**

Yield gap is calculated as:

`Yield Gap = Actual Yield - Trend Yield`

**Step 3: Calculate the Z-score**

The Z-score measures how far the yield gap deviates from its mean in terms of standard deviations.

**Step 4: Identify anomalies**

Years with Z-scores below -1.5 are initially flagged as unusually poor-yield years.

If fewer than three anomalies are detected, the threshold is relaxed to -1.0.

This approach helps identify years where actual yield falls substantially below the estimated historical trend.

## 📈 Time-Series Forecasting

The project uses the ARIMA (AutoRegressive Integrated Moving Average) model to forecast rice yield for the next three years.

The model consists of three components:

* **AR:** Uses previous observations.
* **I:** Uses differencing to address non-stationarity.
* **MA:** Uses previous forecast errors.

The Augmented Dickey-Fuller (ADF) test is used to examine stationarity before selecting the differencing order.

The forecast is generated using historical yield observations.

## 🛠️ Technology Stack

| Technology  | Application                         |
| ----------- | ----------------------------------- |
| Python      | Main programming language           |
| Pandas      | Data manipulation and cleaning      |
| NumPy       | Numerical calculations              |
| Matplotlib  | Data visualization                  |
| Seaborn     | Statistical visualization           |
| SciPy       | Statistical testing                 |
| Statsmodels | Regression and time-series analysis |
| CSV         | Dataset storage                     |

## 📂 Repository Structure

```text
Crop-Yield-Anomaly-Analysis/
│
├── Custom_Crops_yield_Historical_Dataset.csv
├── cleaned_crop_data.csv
│
├── data_cleaning.py
├── visualization.py
├── stats_analysis.py
│
├── requirements.txt
├── README.md
│
├── graphs/
│   ├── 1_yield_trend_anomalies.png
│   ├── 2_rain_vs_gap.png
│   ├── 3_rain_boxplot.png
│   ├── 4_rain_group_bar.png
│   ├── 5_smoothing.png
│   └── 6_arima_forecast.png
│
└── yearly_results.csv
```

*The graphs and yearly results are generated when the statistical analysis script is executed.*

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/4piripiri/Crop-Yield-Anomaly-Analysis.git
```

### 2. Navigate to the Project Folder

```bash
cd Crop-Yield-Anomaly-Analysis
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Project

Execute the scripts in the following order:

**Step 1 — Data Cleaning**

```bash
python data_cleaning.py
```

**Step 2 — Data Visualization**

```bash
python visualization.py
```

**Step 3 — Statistical Analysis**

```bash
python stats_analysis.py
```

## 📁 Project Outputs

The project generates:

* Cleaned agricultural dataset.
* Annual rice-yield statistics.
* Identified anomaly years.
* Rainfall and temperature correlation results.
* Statistical hypothesis-testing results.
* Regression analysis results.
* Moving average and exponential smoothing values.
* Three-year ARIMA yield forecast.
* Six statistical visualization graphs.
* `yearly_results.csv` containing yearly analysis results.

## ⚠️ Limitations

* The analysis focuses on Rice rather than all agricultural crops.
* Rainfall and temperature are not the only factors influencing crop yield.
* Correlation does not establish causation.
* Statistical results depend on the quality and availability of historical data.
* ARIMA forecasts based on historical yield patterns may not capture unexpected environmental changes.
* The anomaly detection threshold influences which years are classified as poor-yield years.

## 🔮 Future Scope

Possible improvements include:

* Extending the analysis to multiple crops.
* Incorporating soil quality and irrigation information.
* Integrating real-time weather datasets.
* Exploring machine learning techniques for anomaly detection.
* Comparing multiple forecasting models.
* Developing an interactive dashboard using Streamlit or Power BI.

## 🎓 Learning Outcomes

This project demonstrates practical applications of:

* Python programming.
* Data cleaning and preprocessing.
* Exploratory Data Analysis.
* Statistical hypothesis testing.
* Correlation and regression analysis.
* Anomaly detection.
* Time-series analysis.
* Data visualization.
* Agricultural data analytics.

## 👩‍💻 Project Information

**Project Title:** Crop Yield Anomaly Analysis

**Domain:** Data Analytics / Agricultural Analytics

**Programming Language:** Python

**Course:** Python Programming Laboratory — Capstone Project

**Repository:** https://github.com/4piripiri/Crop-Yield-Anomaly-Analysis

---

*Developed for academic and educational purposes.*
