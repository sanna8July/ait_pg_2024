# Example 1: Loading a CSV file into a DataFrame
# from pathlib import Path
#
# print(Path.cwd())
# Path.cwd().parents[1].joinpath("datasets/cars.csv")

import pandas as pd
from joblib import Parallel, delayed

# Load a CSV file into a DataFrame
df = pd.read_csv('datasets/cars.csv')

row_num = df.shape[0]
num_a = int(row_num / 3)
num_b = int(row_num / 3)
num_c = row_num - num_a - num_b

letter_a = ['A'] * num_a
letter_b = ['B'] * num_b
letter_c = ['C'] * num_c
letters = letter_a + letter_b + letter_c

print(len(letters))

df["target"] = letters


# Display the first few rows of the DataFrame
print(df.head())
print(df.tail())
pd.set_option('display.max_columns', 9)
# In this example, we use the read_csv function from Pandas to load a CSV file named data.csv into a DataFrame.

# Example 2: Exploring DataFrame Information

# Display the column names and data types
print("Column Names and Data Types:")
print(df.dtypes)

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Display the shape of the DataFrame
print("\nDataFrame Shape:", df.shape)
# Here, we explore information about the DataFrame, such as column names, data types, summary statistics, and the shape of the DataFrame.

# squares_parallel = Parallel(n_jobs=-1)(delayed(calculate_square)(i, num) for i, num in enumerate(numbers))

# Example 3: Selecting and Filtering Data
df.groupby('acceleration')

# Select a single column
column_data = df[['mpg', 'displacement']].groupby('displacement').mean()

# Select multiple columns
multiple_columns = df[['acceleration', 'year']]

# Filter rows based on a condition
filtered_data = df[df['displacement'] > 10]
# In this example, we demonstrate how to select specific columns and filter rows based on conditions in the DataFrame.

# Example 4: Grouping and Aggregating Data

# Group data by a column and calculate mean
mean_by_group = df.groupby(['year']).mean(True)

# Perform multiple aggregations
agg_results = df.groupby('displacement').agg({'weight': 'mean', 'horsepower': 'sum'})

# squares_parallel = Parallel(n_jobs=-1)(delayed(calculate_square)(i, num) for i, num in enumerate(numbers))
# Here, we group the data by a column and perform aggregations such as mean calculation and summing across multiple columns.

# Example 5: Handling Missing Values

# Drop rows with missing values
df_dropna = df.dropna()

# Fill missing values with a specified value
df_fillna = df.fillna(0)
# In this example, we demonstrate how to handle missing values by either dropping rows with missing values or filling them with a specified value.
