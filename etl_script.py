import pandas as pd
from pathlib import Path

# Correct path to CSV File
DATA_PATH = Path("data/retail_sales_dataset.csv")

# Load the CSV file in a pandas DataFrame
df = pd.read_csv(DATA_PATH)

# Display basic info and first few rows
print(df.info())
print(df.head())

# Clean and Transform Data
df['Date'] = pd.to_datetime(df['Date'], errors='coerce') # Convert date column to proper datetime
df = df.dropna() # Remove rows with missing data

# Add calculated colums
df['Revenue'] = df['Quantity'] * df['Price per Unit']

# Example of grouping and aggregation
sales_by_category = df.groupby('Product Category')['Revenue'].sum().reset_index()

print(sales_by_category)
