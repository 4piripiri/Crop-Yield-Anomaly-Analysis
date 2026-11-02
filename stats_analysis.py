import sys
import warnings
import matplotlib
matplotlib.use("Agg")  
warnings.filterwarnings("ignore")   
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA

df = pd.read_csv("cleaned_crop_data.csv")
crop = sys.argv[1] if len(sys.argv) > 1 else df["Crop"].value_counts().index[0]
df = df[df["Crop"] == crop]
print("1. Crop:", crop)

cols = ["Yield_kg_per_ha", "Rainfall_mm", "Temperature_C"]
data = df.groupby("Year")[cols].mean()
data.columns = ["yield", "rain", "temp"]

print("\n2: Descriptive statistics")
print(data.describe().round(2))

slope, intercept, r, p, se = stats.linregress(data.index, data["yield"])
data["trend"] = intercept + slope * data.index
data["gap"] = data["yield"] - data["trend"]          # gap from trend
data["z"] = stats.zscore(data["gap"])                # gap in standard deviations
data["anomaly"] = data["z"] < -1.5                   # unusually poor year
if data["anomaly"].sum() < 3:                        # too few -> be less strict
    data["anomaly"] = data["z"] < -1.0
    print("(Used z < -1.0 because very few years were below -1.5)")
print("\n3: Poor-yield (anomaly) years")
print(data[data["anomaly"]][["yield", "trend", "z"]].round(2))

print("\n4: Is the gap normally distributed? (Shapiro-Wilk)")
w, p = stats.shapiro(data["gap"])
print("p =", round(p, 3), "->", "normal" if p > 0.05 else "not normal")

print("\n5: Correlation of yield gap with weather (Pearson)")
for f in ["rain", "temp"]:
    r, p = stats.pearsonr(data["gap"], data[f])
    print(f, ": r =", round(r, 3), " p =", round(p, 4),
          "-> significant" if p < 0.05 else "-> not significant")

print("\n6: Weather in anomaly years vs normal years")
bad = data[data["anomaly"]]
good = data[~data["anomaly"]]
for f in ["rain", "temp"]:
    lev = stats.levene(bad[f], good[f]).pvalue        # are the spreads equal?
    t, p = stats.ttest_ind(bad[f], good[f], equal_var=(lev > 0.05))
    u, pu = stats.mannwhitneyu(bad[f], good[f])       # backup test, no normality needed
    print(f, ": mean bad =", round(bad[f].mean(), 1), " mean normal =", round(good[f].mean(), 1),
          " t-test p =", round(p, 4), " Mann-Whitney p =", round(pu, 4))

t, p = stats.ttest_1samp(bad["yield"], data["yield"].mean())
print("One-sample t-test (bad-year yield vs overall mean): p =", round(p, 4))

before = data["rain"].shift(1)[data["anomaly"]].dropna()
now = data["rain"][before.index]
if len(before) >= 3:
    t, p = stats.ttest_rel(now, before)
    print("Paired t-test (rain in bad year vs year before): p =", round(p, 4))

print("\n7: Split years into LOW / MEDIUM / HIGH rainfall")
data["rain_group"] = pd.qcut(data["rain"], 3, labels=["low", "medium", "high"])
print(data.groupby("rain_group", observed=True)["gap"].mean().round(1))
groups = [g["gap"].values for _, g in data.groupby("rain_group", observed=True)]
f, p = stats.f_oneway(*groups)
print("ANOVA: does the yield gap differ between rain groups? p =", round(p, 4))
h, p = stats.kruskal(*groups)
print("Kruskal-Wallis (non-parametric ANOVA): p =", round(p, 4))
table = pd.crosstab(data["anomaly"], data["rain_group"])
chi2, p, dof, exp = stats.chi2_contingency(table)
print("Chi-square: are anomaly years linked to rain group? p =", round(p, 4))

print("\n8: Regression  (yield gap ~ rain + temp)")
X = sm.add_constant(data[["rain", "temp"]])
model = sm.OLS(data["gap"], X).fit()
print("R-squared =", round(model.rsquared, 3), "(share of yield variation explained by weather)")
print(model.pvalues.round(4))

print("\n9: Smoothing")
data["SMA_3"] = data["yield"].rolling(3).mean()     
data["EWMA"] = data["yield"].ewm(alpha=0.4).mean()   
print(data[["yield", "SMA_3", "EWMA"]].tail(5).round(1))

print("\n10: Stationarity (ADF test)")
p = adfuller(data["yield"])[1]
print("Original series p =", round(p, 3), "->", "stationary" if p < 0.05 else "NOT stationary")
d = 0
series = data["yield"]
while adfuller(series)[1] > 0.05 and d < 2:          
    series = series.diff().dropna()
    d += 1
    print("After differencing", d, "time(s): p =", round(adfuller(series)[1], 3))
model = ARIMA(data["yield"].values, order=(1, d, 1)).fit()
print("\nForecast for next 3 years (kg/ha):", model.forecast(3).round(0))


os.makedirs("graphs", exist_ok=True)

plt.figure(figsize=(9, 4))
plt.plot(data.index, data["yield"], label="Yield")
plt.plot(data.index, data["trend"], "--", label="Trend line")
plt.scatter(data.index[data["anomaly"]], data["yield"][data["anomaly"]], color="red", zorder=3, label="Poor year")
plt.title(crop + ": yield, trend and poor years"); plt.xlabel("Year"); plt.ylabel("kg/ha"); plt.legend()
plt.tight_layout(); plt.savefig("graphs/1_yield_trend_anomalies.png", dpi=150); plt.close()

plt.figure(figsize=(6, 4))
plt.scatter(data["rain"], data["gap"])
m, c = np.polyfit(data["rain"], data["gap"], 1)
plt.plot(data["rain"], m * data["rain"] + c, color="red")
plt.title("Rainfall vs yield gap"); plt.xlabel("Rainfall (mm)"); plt.ylabel("Yield gap from trend (kg/ha)")
plt.tight_layout(); plt.savefig("graphs/2_rain_vs_gap.png", dpi=150); plt.close()

plt.figure(figsize=(5, 4))
plt.boxplot([good["rain"], bad["rain"]])
plt.xticks([1, 2], ["Normal years", "Poor years"])
plt.title("Rainfall: normal vs poor years"); plt.ylabel("Rainfall (mm)")
plt.tight_layout(); plt.savefig("graphs/3_rain_boxplot.png", dpi=150); plt.close()

plt.figure(figsize=(5, 4))
data.groupby("rain_group", observed=True)["gap"].mean().plot(kind="bar", color=["#d9534f", "#999999", "#5cb85c"])
plt.title("Yield gap by rainfall group"); plt.ylabel("Mean gap (kg/ha)"); plt.xticks(rotation=0)
plt.tight_layout(); plt.savefig("graphs/4_rain_group_bar.png", dpi=150); plt.close()

plt.figure(figsize=(9, 4))
plt.plot(data.index, data["yield"], alpha=0.5, label="Yield")
plt.plot(data.index, data["SMA_3"], label="3-year SMA")
plt.plot(data.index, data["EWMA"], label="EWMA")
plt.title("Smoothing"); plt.legend(); plt.tight_layout()
plt.savefig("graphs/5_smoothing.png", dpi=150); plt.close()

fc = model.get_forecast(3)
future = [data.index[-1] + i for i in (1, 2, 3)]
band = np.asarray(fc.conf_int())
plt.figure(figsize=(9, 4))
plt.plot(data.index, data["yield"], label="Actual")
plt.plot(future, fc.predicted_mean, "r--o", label="Forecast")
plt.fill_between(future, band[:, 0], band[:, 1], color="red", alpha=0.2, label="95% range")
plt.title("ARIMA forecast"); plt.legend(); plt.tight_layout()
plt.savefig("graphs/6_arima_forecast.png", dpi=150); plt.close()
print("Saved 6 graphs in the graphs folder")

data.to_csv("yearly_results.csv")
print("\nSaved yearly_results.csv")