import pandas as pd

df = pd.read_csv("data/stroke_data.csv")

# Check for 'Diagnosis' or 'stroke' column
target_col = "stroke" if "stroke" in df.columns else "Diagnosis"

print(f"Class distribution for '{target_col}':")
print(df[target_col].value_counts())
print(f"\nPercentage:")
print(df[target_col].value_counts(normalize=True) * 100)
print(f"\nTotal samples: {len(df)}")
print(
    f"\nImbalance Ratio: {df[target_col].value_counts()[0] / df[target_col].value_counts()[1]:.2f}:1"
)
