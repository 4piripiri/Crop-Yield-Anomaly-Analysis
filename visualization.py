"""
visualization.py

Responsible for: charts that reveal patterns in yield vs. rainfall/temperature.
Rubric criterion covered: Data Visualization (Matplotlib/Seaborn).
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pathlib import Path

FIGURES_DIR = Path(__file__).resolve().parent.parent / "outputs" / "figures"


def plot_yield_over_time(df: pd.DataFrame, year_col: str, yield_col: str, save_as: str = "yield_over_time.png"):
    """
    Line chart of yield across years — the starting point for spotting anomaly years.
    Highlight anomaly years (see stats_analysis.detect_anomaly_years) once identified.
    """
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df, x=year_col, y=yield_col, marker="o")
    plt.title("Crop Yield Over Time")
    plt.xlabel("Year")
    plt.ylabel("Yield")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / save_as)
    plt.close()


def plot_yield_vs_factor(df: pd.DataFrame, factor_col: str, yield_col: str, save_as: str = None):
    """
    Scatter plot of yield vs. a single environmental factor (rainfall or temperature),
    with a regression line to visually suggest correlation strength.
    """
    save_as = save_as or f"yield_vs_{factor_col}.png"
    plt.figure(figsize=(8, 6))
    sns.regplot(data=df, x=factor_col, y=yield_col, scatter_kws={"alpha": 0.6})
    plt.title(f"Yield vs {factor_col.capitalize()}")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / save_as)
    plt.close()


def plot_correlation_heatmap(df: pd.DataFrame, columns: list, save_as: str = "correlation_heatmap.png"):
    """Heatmap of correlations between yield and all environmental factors at once."""
    plt.figure(figsize=(8, 6))
    corr = df[columns].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / save_as)
    plt.close()

    # TODO: add one more chart type of your choice — e.g. a boxplot of yield
    # by anomaly-year vs normal-year, once stats_analysis flags them.
