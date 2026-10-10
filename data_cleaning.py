import argparse
from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent
DEFAULT_INPUT = PROJECT_DIR / "Custom_Crops_yield_Historical_Dataset.csv"
DEFAULT_OUTPUT = PROJECT_DIR / "cleaned_crop_data.csv"
REQUIRED_COLUMNS = {
    "Year",
    "State Name",
    "Dist Name",
    "Crop",
    "Area_ha",
    "Yield_kg_per_ha",
}
TEXT_COLUMNS = ("State Name", "Dist Name", "Crop")


def clean_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the crop dataset while preserving added columns."""
    cleaned = df.copy().drop_duplicates()

    text_columns = cleaned.select_dtypes(include=["object", "string"]).columns
    for column in text_columns:
        cleaned[column] = cleaned[column].astype("string").str.strip()
        cleaned[column] = cleaned[column].replace("", pd.NA)

    required_columns = [column for column in REQUIRED_COLUMNS if column in cleaned]
    if required_columns:
        cleaned = cleaned.dropna(subset=required_columns)

    for column, minimum in (("Area_ha", 0), ("Yield_kg_per_ha", 0)):
        if column in cleaned:
            cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")
            cleaned = cleaned.dropna(subset=[column])
            cleaned = cleaned.loc[cleaned[column] > minimum] if column == "Area_ha" else cleaned.loc[cleaned[column] >= minimum]

    numeric_features = cleaned.select_dtypes(include="number").columns
    for column in numeric_features:
        if cleaned[column].isna().any():
            if column.lower().endswith(("id", "code")) or column.lower() == "year":
                fill_value = cleaned[column].mode().iloc[0] if not cleaned[column].mode().empty else None
            else:
                fill_value = cleaned[column].median()
            if fill_value is not None and pd.notna(fill_value):
                cleaned[column] = cleaned[column].fillna(fill_value)

    for column in text_columns:
        if cleaned[column].isna().any():
            modes = cleaned[column].mode()
            cleaned[column] = cleaned[column].fillna(modes.iloc[0] if not modes.empty else "Unknown")

    return cleaned.reset_index(drop=True)


def clean_crop_csv(
    input_path: str | Path = DEFAULT_INPUT,
    output_path: str | Path = DEFAULT_OUTPUT,
) -> pd.DataFrame:
    """Read, clean, and export a crop CSV; return the cleaned data."""
    input_path = Path(input_path)
    output_path = Path(output_path)
    if input_path.resolve() == output_path.resolve():
        raise ValueError("Input and output paths must be different to protect the source CSV.")

    source = pd.read_csv(input_path)
    cleaned = clean_pipeline(source)
    cleaned.to_csv(output_path, index=False)

    print(f"Loaded {len(source):,} rows from {input_path}")
    print(f"Rows: {len(source):,} -> {len(cleaned):,} ({len(source) - len(cleaned):,} removed)")
    print(f"Duplicate rows found: {int(source.duplicated().sum()):,}")
    print(
        "Missing cells: "
        f"{int(source.isna().sum().sum()):,} -> {int(cleaned.isna().sum().sum()):,}"
    )
    print(f"Refined CSV saved to {output_path}")
    return cleaned


def clean_crop_dataset(
    input_path: str | Path = DEFAULT_INPUT,
    output_path: str | Path = DEFAULT_OUTPUT,
) -> pd.DataFrame:
    """Alias for clean_crop_csv with a dataset-oriented name."""
    return clean_crop_csv(input_path, output_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Clean a crop data CSV.")
    parser.add_argument("input", nargs="?", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("output", nargs="?", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    clean_crop_csv(args.input, args.output)


if __name__ == "__main__":
    main()
