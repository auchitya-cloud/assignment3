import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Create a random dataset of 100 rows and 30 columns.
np.random.seed(42)  # For reproducibility
dataset = pd.DataFrame(np.random.randint(1, 201, size=(100, 30)), columns=[f'col{i}' for i in range(1, 31)])

# Step 2: Replace all the values with NA in the dataset defined between [10, 60].
dataset.loc[:, 'col10':'col60'] = np.nan

# Step 3: Print the count of number rows having missing values.
num_rows_with_missing_values = dataset.isnull().any(axis=1).sum()
print(f"Number of rows with missing values: {num_rows_with_missing_values}")

# Step 4: Replace all the NA values with the average of the column value.
dataset.fillna(dataset.mean(), inplace=True)

# Step 5: Find the Pearson correlation among all the columns and plot a heatmap.
correlation_matrix = dataset.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Pearson Correlation Heatmap")
plt.show()

# Step 6: Select those columns having correlation <= 0.7.
columns_with_low_correlation = correlation_matrix.columns[correlation_matrix.max() <= 0.7]
print("Columns with correlation <= 0.7:")
print(columns_with_low_correlation)

# Step 7: Normalize all the values in the dataset between 0 and 10.
dataset_normalized = (dataset - dataset.min()) / (dataset.max() - dataset.min()) * 10

# Step 8: Replace all the values in the dataset with 1 if value <= 0.5 else with 0.
dataset_binary = dataset_normalized.applymap(lambda x: 1 if x <= 0.5 else 0)

# Display the processed datasets
print("\nNormalized Dataset (between 0 and 10):")
print(dataset_normalized)
print("\nBinary Dataset (0 or 1 based on threshold 0.5):")
print(dataset_binary)
