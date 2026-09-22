"""
stats_analysis.py

Responsible for: (1) flagging unusually poor yield years, (2) testing whether
rainfall/temperature explain those dips.
Rubric criterion covered: Statistical Analysis / Forecasting (SciPy/Statsmodels).
"""

import pandas as pd
import numpy as np
from scipy import stats


def detect_anomaly_years(df: pd.DataFrame, yield_col: str, year_col: str, z_thresh: float = -1.5) -> pd.DataFrame:
    """
    Flag years where yield is unusually low, using a z-score threshold.

    A z-score below `z_thresh` (default -1.5 std devs from the mean) is
    considered an anomalous "poor yield" year. Tune the threshold and justify
    your choice in the report.

    Returns:
        DataFrame with an added 'yield_zscore' and 'is_anomaly' column.
    """
    df = df.copy()
    df["yield_zscore"] = stats.zscore(df[yield_col])
    df["is_anomaly"] = df["yield_zscore"] < z_thresh
    return df


def correlate_yield_with_factor(df: pd.DataFrame, yield_col: str, factor_col: str) -> dict:
    """
    Pearson correlation between yield and one environmental factor
    (e.g. rainfall or temperature), with the p-value so you can say
    whether the relationship is statistically significant.

    Returns:
        {"r": correlation coefficient, "p_value": p-value}
    """
    r, p_value = stats.pearsonr(df[yield_col], df[factor_col])
    return {"r": r, "p_value": p_value}


def compare_anomaly_vs_normal_years(df: pd.DataFrame, factor_col: str) -> dict:
    """
    T-test comparing `factor_col` (e.g. rainfall) between anomaly years and
    normal years. Requires detect_anomaly_years() to have been run first
    (needs an 'is_anomaly' column).

    A significant difference (p < 0.05) supports the claim that this factor
    contributed to poor-yield years.
    """
    anomaly_vals = df.loc[df["is_anomaly"], factor_col]
    normal_vals = df.loc[~df["is_anomaly"], factor_col]
    t_stat, p_value = stats.ttest_ind(anomaly_vals, normal_vals, equal_var=False)
    return {"t_stat": t_stat, "p_value": p_value}


def check_stationarity(series: pd.Series) -> dict:
    """
    Augmented Dickey-Fuller test — required before any ARIMA-style forecasting
    (the rubric explicitly calls this out under "Excellent"). If p > 0.05,
    the series is non-stationary and needs differencing before forecasting.

    TODO: from statsmodels.tsa.stattools import adfuller
          result = adfuller(series.dropna())
          return {"adf_stat": result[0], "p_value": result[1]}
    """
    raise NotImplementedError("Implement using statsmodels.tsa.stattools.adfuller")


def forecast_yield(series: pd.Series, order: tuple = (1, 1, 1), steps: int = 3):
    """
    Fit an ARIMA model on the yield time series and forecast `steps` years ahead.

    TODO: from statsmodels.tsa.arima.model import ARIMA
          model = ARIMA(series, order=order).fit()
          forecast = model.forecast(steps=steps)
          return forecast

    Remember to run check_stationarity() first and difference the series
    (increase the 'd' in `order`) if it's non-stationary — this is exactly
    what separates a "Good" from an "Excellent" on this rubric criterion.
    """
    raise NotImplementedError("Implement ARIMA forecasting with statsmodels")
