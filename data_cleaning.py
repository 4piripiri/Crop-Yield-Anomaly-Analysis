import pandas as pd

# 1. Load the original CSV directly from the main folder
df = pd.read_csv("Custom_Crops_yield_Historical_Dataset.csv")
print("Data loaded successfully.")

# 2. Inspect dimensions and data types
print("Shape:", df.shape)
print("Data Types:\n", df.dtypes)

# 3. Check and remove duplicate rows
duplicates = df.duplicated().sum()
print(f"Found {duplicates} duplicate rows. Removing them...")
df = df.drop_duplicates()

# 4. Handle missing values
if "Average_Rainfall" in df.columns:
    df["Average_Rainfall"] = df["Average_Rainfall"].fillna(df["Average_Rainfall"].mean())
if "Mean_Temperature" in df.columns:
    df["Mean_Temperature"] = df["Mean_Temperature"].fillna(df["Mean_Temperature"].mean())

df = df.dropna(subset=["Production", "Area"])

# 5. Correct inconsistent category names
df["State_Name"] = df["State_Name"].str.strip().str.title()
df["Crop"] = df["Crop"].str.strip().str.title()

# 6. Create Yield column
df["Yield"] = df["Production"] / df["Area"]
print("Created 'Yield' column.")

# 7. Export the cleaned dataset directly to the main folder
df.to_csv("cleaned_crop_data.csv", index=False)
print("Cleaned data saved as cleaned_crop_data.csv")
