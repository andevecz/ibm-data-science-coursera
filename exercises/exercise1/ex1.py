import pandas as pd
from pathlib import Path

csv_path = Path(__file__).parent / 'file1.csv'

df = pd.read_csv(csv_path)
print("DataFrame: " ,df.head(), sep="\n")

new_df = df[["Age"]]
print("\nNew DataFrame: " ,new_df.head(), sep="\n")

first_value = df.iloc[0,0]
print(f"\nFirst value of the DataFrame: {first_value}")

first_age = df.loc[0,"Age"]
print(f"\nFirst age in the DataFrame: {first_age}")

first_name_age = df.loc[0, "Name":"Age"]
print(f"\nFirst name and age: ", first_name_age.head(), sep="\n")

