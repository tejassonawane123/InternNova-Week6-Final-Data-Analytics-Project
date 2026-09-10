import pandas as pd
import os

dataset_path = "Dataset"

for file in os.listdir(dataset_path):
    if file.endswith(".csv"):
        file_path = os.path.join(dataset_path, file)
        df = pd.read_csv(file_path)

        print("=" * 70)
        print("FILE:", file)
        print("Rows:", df.shape[0])
        print("Columns:", df.shape[1])
        print("Column Names:", list(df.columns))
        print("Data Types:")
        print(df.dtypes)
        print("Missing Values:")
        print(df.isnull().sum())
        print("Duplicate Rows:", df.duplicated().sum())
        print()