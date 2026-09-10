import pandas as pd

input_file = "Dataset/olist_geolocation_dataset.csv"
output_file = "Dataset/olist_geolocation_cleaned.csv"

df = pd.read_csv(input_file)

before = len(df)

df = df.drop_duplicates()

after = len(df)

df.to_csv(output_file, index=False)

print("Geolocation dataset prepared successfully.")
print("Rows before cleaning:", before)
print("Rows after cleaning:", after)
print("Duplicates removed:", before - after)
print("Columns:", df.shape[1])
print("Duplicate rows after preparation:", df.duplicated().sum())