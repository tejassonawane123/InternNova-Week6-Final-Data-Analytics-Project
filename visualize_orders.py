import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset/olist_orders_eda.csv')
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

# 1. Order Status
df['order_status'].value_counts().plot(kind='bar')
plt.title('Order Status Distribution')
plt.xlabel('Order Status')
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.savefig('Outputs/order_status.png')
plt.close()

# 2. Monthly Orders
df.groupby(df['order_purchase_timestamp'].dt.to_period('M')).size().plot()
plt.title('Monthly Order Trend')
plt.xlabel('Month')
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.savefig('Outputs/monthly_orders.png')
plt.close()

# 3. Delivery Days
df['delivery_days'].plot(kind='hist', bins=30)
plt.title('Delivery Days Distribution')
plt.xlabel('Delivery Days')
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.savefig('Outputs/delivery_days.png')
plt.close()

# 4. Actual vs Estimated Delivery
plt.scatter(df['estimated_days'], df['delivery_days'], s=5)
plt.title('Actual vs Estimated Delivery Days')
plt.xlabel('Estimated Days')
plt.ylabel('Actual Delivery Days')
plt.tight_layout()
plt.savefig('Outputs/delivery_comparison.png')
plt.close()

# 5. Delivery Performance
df['delivery_result'] = df['delivery_days'] <= df['estimated_days']
df['delivery_result'].map({True:'On Time', False:'Late'}).value_counts().plot(kind='bar')
plt.title('On-Time vs Late Delivery')
plt.xlabel('Delivery Result')
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.savefig('Outputs/Task 5/delivery_performance.png')
plt.close()

print('5 visualizations created successfully.')