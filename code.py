import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv('sales_data_sample.csv', encoding='latin1')  
print("Original Dataset Shape:", df.shape)

# Step 2: Initial data inspection
print("\nInitial Info:")
print(df.info())
print("\nFirst 5 Rows:")
print(df.head())

# Step 3: Handle missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Drop rows with missing values
df.dropna(inplace=True)
print("\nMissing values after dropping nulls:")
print(df.isnull().sum())

# Step 4: Remove duplicate rows
before = df.shape[0]
df.drop_duplicates(inplace=True)
after = df.shape[0]
print(f"\nRemoved {before - after} duplicate rows.")

# Step 5: Standardize text values
text_cols = ['STATUS', 'PRODUCTLINE', 'DEALSIZE']
for col in text_cols:
    if col in df.columns:
        df[col] = df[col].str.strip().str.upper()

# Step 6: Convert date columns
if 'ORDERDATE' in df.columns:
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], dayfirst=True, errors='coerce')

# Step 7: Rename column headers
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

# Step 8: Fix data types
if 'quantityordered' in df.columns:
    df['quantityordered'] = df['quantityordered'].astype(int)

# Step 9: Final data check
print("\nCleaned Dataset Shape:", df.shape)
print("\nCleaned Data Info:")
print(df.info())

# Step 10: Save cleaned dataset
df.to_csv('cleaned_sales_data.csv', index=False)
print("\n✅ Cleaned data saved as 'cleaned_sales_data.csv'")

print(df.info())

# Step 10: Save cleaned dataset
df.to_csv('cleaned_sales_data.csv', index=False)
print("\n✅ Cleaned data saved as 'cleaned_sales_data.csv'")
