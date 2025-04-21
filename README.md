# DataAnalyst_task1
📌 Goal:
To clean and prepare the raw sales dataset so it's ready for analysis.

🧰 Tools Used:
Python

Pandas library

📂 Dataset:
sales_data_sample.csv (sales data with dates, status, product info, etc.)

✅ What This Code Does:
Loads the data from the CSV file.

Checks for missing values and removes rows that have any.

Removes duplicate rows from the data.

Cleans text columns like STATUS, PRODUCTLINE, and DEALSIZE by making them uppercase and removing extra spaces.

Converts the order date into a proper date format.

Renames all column headers to be lowercase and replace spaces with underscores (e.g., Order Date → order_date).

Fixes data types, like changing quantityordered to integer.

Saves the cleaned dataset to a new CSV file: cleaned_sales_data.csv.

📤 Output File:
cleaned_sales_data.csv – this file is clean and ready for analysis.
