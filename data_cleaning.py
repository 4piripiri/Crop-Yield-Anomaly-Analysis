"""
data_cleaning.py

Responsible for: handling missing values, duplicates, and outliers.
Rubric criterion covered: Data Cleaning & Manipulation (NumPy/Pandas).
"""

import pandas as pd
import numpy as np


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove exact duplicate rows. Print how many were dropped for the report."""
    before = len(df)
    df = df.drop_duplicates()
    print(f"Dropped {before - len(df)} duplicate rows")
    return df


def handle_missing_values(df: pd.DataFrame, strategy: str = "median") -> pd.DataFrame:
    """
    Fill or drop missing values.

    TODO: decide per-column whether to fill (e.g. fillna with median/mean for
    rainfall/temperature) or drop rows (e.g. if 'yield' itself is missing —
    you probably can't impute the target variable).

    Args:
        df: input DataFrame
        strategy: "median", "mean", or "drop"
    """
    # TODO: implement. Example starting point:
    # numeric_cols = df.select_dtypes(include=[np.number]).columns
    # if strategy == "drop":
    #     df = df.dropna(subset=numeric_cols)
    # else:
    #     df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].agg(strategy))
    raise NotImplementedError("Fill in missing value strategy")


def remove_outliers_iqr(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Remove outliers in `column` using the IQR method (rows outside
    Q1 - 1.5*IQR to Q3 + 1.5*IQR are dropped).

    Useful for rainfall/temperature columns that may have sensor errors.
    """
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    mask = df[column].between(lower, upper)
    print(f"{column}: removed {(~mask).sum()} outlier rows (bounds: {lower:.2f} to {upper:.2f})")
    return df[mask]


def clean_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """Run the full cleaning pipeline in sequence. Wire up your functions here."""
    df = drop_duplicates(df)
    # df = handle_missing_values(df)
    # df = remove_outliers_iqr(df, "rainfall")
    # df = remove_outliers_iqr(df, "temperature")
    return df
