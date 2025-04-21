import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv('sales_data_sample.csv', encoding='latin1')  # Adjust encoding if needed
print("Original Dataset Shape:", df.shape)

# Step 2: Display initial info
print("\nInitial Info:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())

# Step 3: Check and handle missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Drop rows with any missing values
df.dropna(inplace=True)
print("\nMissing values after dropping nulls:")
print(df.isnull().sum())

# Step 4: Remove duplicates
initial_shape = df.shape
df.drop_duplicates(inplace=True)
print(f"\nRemoved {initial_shape[0] - df.shape[0]} duplicate rows.")

# Step 5: Standardize text fields if applicable
text_columns = ['STATUS', 'PRODUCTLINE', 'DEALSIZE']
for col in text_columns:
    if col in df.columns:
        df[col] = df[col].str.strip().str.upper()

# Step 6: Convert date columns
if 'ORDERDATE' in df.columns:
    df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], dayfirst=True, errors='coerce')

# Step 7: Clean column names
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

# Step 8: Fix data types (if needed)
if 'quantityordered' in df.columns:
    df['quantityordered'] = df['quantityordered'].astype(int)

# Step 9: Final info
print("\nCleaned Dataset Shape:", df.shape)
print("\nCleaned Data Info:")
print(df.info())

# Step 10: Save cleaned dataset
df.to_csv('cleaned_sales_data.csv', index=False)
print("\n✅ Cleaned data saved as 'cleaned_sales_data.csv'")
