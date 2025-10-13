import kagglehub
import pandas as pd
import os
import shutil

# Download dataset from Kaggle
print("Downloading dataset from Kaggle...")
path = kagglehub.dataset_download("teamincribo/stroke-prediction")
print(f"Dataset downloaded to: {path}")

# Find the CSV file
csv_files = [f for f in os.listdir(path) if f.endswith(".csv")]
if not csv_files:
    raise FileNotFoundError("No CSV file found in downloaded dataset")

source_file = os.path.join(path, csv_files[0])
dest_file = "data/stroke_data.csv"

# Copy to our data folder
shutil.copy(source_file, dest_file)
print(f"Dataset copied to: {dest_file}")

# Load and explore
df = pd.read_csv(dest_file)
print(f"\nDataset shape: {df.shape}")
print(f"\nColumns:\n{df.columns.tolist()}")
print(f"\nFirst few rows:\n{df.head()}")
print(f"\nData types:\n{df.dtypes}")
print(f"\nMissing values:\n{df.isnull().sum()}")
