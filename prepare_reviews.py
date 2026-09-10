import pandas as pd

input_file = "Dataset/olist_order_reviews_dataset.csv"
output_file = "Dataset/olist_order_reviews_cleaned.csv"

df = pd.read_csv(input_file)

df["review_comment_title"] = df["review_comment_title"].fillna("No Title")
df["review_comment_message"] = df["review_comment_message"].fillna("No Review Message")

df["review_creation_date"] = pd.to_datetime(
    df["review_creation_date"],
    errors="coerce"
)

df["review_answer_timestamp"] = pd.to_datetime(
    df["review_answer_timestamp"],
    errors="coerce"
)

df = df.drop_duplicates()

df.to_csv(output_file, index=False)

print("Order Reviews dataset prepared successfully.")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nMissing values after preparation:")
print(df.isnull().sum())

print("\nDuplicate rows after preparation:", df.duplicated().sum())