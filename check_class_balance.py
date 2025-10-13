import pandas as pd

df = pd.read_csv("data/stroke_data.csv")

print("Class distribution for 'Diagnosis':")
print(df["Diagnosis"].value_counts())
print("\nPercentage:")
print(df["Diagnosis"].value_counts(normalize=True) * 100)
print(f"\nTotal samples: {len(df)}")
