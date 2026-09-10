import pandas as pd

input_file = "Dataset/olist_orders_dataset.csv"
output_file = "Dataset/olist_orders_cleaned.csv"

df = pd.read_csv(input_file)

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    df[column] = pd.to_datetime(
        df[column],
        format="%d-%m-%Y %H:%M",
        errors="coerce"
    )

df = df.drop_duplicates()

df.to_csv(output_file, index=False)

print("Orders dataset prepared successfully.")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nMissing values after preparation:")
print(df.isnull().sum())

print("\nDuplicate rows after preparation:", df.duplicated().sum())