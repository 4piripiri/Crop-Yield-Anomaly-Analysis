"""
main.py — runs the full pipeline end-to-end.

Update the placeholder column names below once you've inspected the actual
Kaggle CSV (run data_loader.inspect_data() first to see real column names).
"""

from data_cleaning import clean_pipeline
from visualization import plot_yield_over_time, plot_yield_vs_factor, plot_correlation_heatmap
from stats_analysis import detect_anomaly_years, correlate_yield_with_factor, compare_anomaly_vs_normal_years
from report_generator import generate_report

# TODO: replace with the actual filename you place in data/raw/
RAW_FILENAME = "crop_yield_weather.csv"

# TODO: replace with actual column names from the dataset
YEAR_COL = "year"
YIELD_COL = "yield"
RAINFALL_COL = "rainfall"
TEMPERATURE_COL = "temperature"


def main():
    df = load_raw_data(RAW_FILENAME)
    inspect_data(df)

    df = clean_pipeline(df)

    df = detect_anomaly_years(df, yield_col=YIELD_COL, year_col=YEAR_COL)
    anomaly_years = df.loc[df["is_anomaly"], YEAR_COL].tolist()
    print("Anomaly years:", anomaly_years)

    rainfall_corr = correlate_yield_with_factor(df, YIELD_COL, RAINFALL_COL)
    temp_corr = correlate_yield_with_factor(df, YIELD_COL, TEMPERATURE_COL)

    plot_yield_over_time(df, YEAR_COL, YIELD_COL)
    plot_yield_vs_factor(df, RAINFALL_COL, YIELD_COL)
    plot_yield_vs_factor(df, TEMPERATURE_COL, YIELD_COL)
    plot_correlation_heatmap(df, [YIELD_COL, RAINFALL_COL, TEMPERATURE_COL])

    generate_report(
        anomaly_years=anomaly_years,
        correlations={"rainfall": rainfall_corr, "temperature": temp_corr},
    )


if __name__ == "__main__":
    main()
