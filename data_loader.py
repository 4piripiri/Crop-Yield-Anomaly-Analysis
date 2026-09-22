"""
data_loader.py

Responsible for: loading the raw dataset from data/raw/ into a pandas DataFrame.
Rubric criterion covered: Problem Definition & Dataset Selection.
"""

import pandas as pd
from pathlib import Path

RAW_DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"


def load_raw_data(filename: str) -> pd.DataFrame:
    """
    Load the raw crop yield / weather CSV from data/raw/.

    Args:
        filename: name of the CSV file inside data/raw/ (e.g. "crop_yield_weather.csv")

    Returns:
        Raw, unmodified DataFrame straight from disk.
    """
    filepath = RAW_DATA_DIR / filename
    df = pd.read_csv(filepath)
    return df


def inspect_data(df: pd.DataFrame) -> None:
    """
    Quick sanity check on a freshly loaded DataFrame — shape, dtypes, missing values.
    Useful for the "Problem Definition & Dataset Selection" writeup: describe
    the dataset's size/complexity here.
    """
    print("Shape:", df.shape)
    print("\nColumn dtypes:\n", df.dtypes)
    print("\nMissing values per column:\n", df.isnull().sum())
    print("\nFirst rows:\n", df.head())
