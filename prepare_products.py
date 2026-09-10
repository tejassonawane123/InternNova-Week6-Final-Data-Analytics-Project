import pandas as pd

input_file = "Dataset/olist_products_dataset.csv"
output_file = "Dataset/olist_products_cleaned.csv"

df = pd.read_csv(input_file)

# Fill missing categorical values
df["product_category_name"] = df["product_category_name"].fillna("Unknown")

# Fill missing numerical values with median
numeric_columns = [
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Remove duplicate rows
df = df.drop_duplicates()

df.to_csv(output_file, index=False)

print("Products dataset prepared successfully.")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nMissing values after preparation:")
print(df.isnull().sum())

print("\nDuplicate rows after preparation:", df.duplicated().sum())