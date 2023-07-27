import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp, wilcoxon, ttest_ind, ranksums

# Step 1: Create a random dataset of 500 rows and 5 columns with values between 5 and 10.
np.random.seed(42)  # For reproducibility
dataset = pd.DataFrame(np.random.uniform(5, 11, size=(500, 5)), columns=[f'col{i}' for i in range(1, 6)])

# Step 2: Perform t-Test on each column.
t_test_results = {}
for col in dataset.columns:
    t_stat, p_value = ttest_1samp(dataset[col], 7.5)  # Assuming a population mean of 7.5 for testing.
    t_test_results[col] = {'t-statistic': t_stat, 'p-value': p_value}

# Step 3: Perform Wilcoxon Signed Rank Test on each column.
wilcoxon_results = {}
for col in dataset.columns:
    statistic, p_value = wilcoxon(dataset[col] - 7.5)  # Assuming a population median of 7.5 for testing.
    wilcoxon_results[col] = {'statistic': statistic, 'p-value': p_value}

# Step 4: Perform Two Sample t-Test and Wilcoxon Rank Sum Test on Column 3 and Column 4.
col3 = dataset['col3']
col4 = dataset['col4']
two_sample_t_test = ttest_ind(col3, col4)
wilcoxon_ranksums_test = ranksums(col3, col4)

# Display the results of all the tests
print("T-Test Results:")
for col, results in t_test_results.items():
    print(f"Column {col}: t-statistic={results['t-statistic']}, p-value={results['p-value']}")

print("\nWilcoxon Signed Rank Test Results:")
for col, results in wilcoxon_results.items():
    print(f"Column {col}: statistic={results['statistic']}, p-value={results['p-value']}")

print("\nTwo Sample T-Test Results for Column 3 and Column 4:")
print(f"t-statistic={two_sample_t_test.statistic}, p-value={two_sample_t_test.pvalue}")

print("\nWilcoxon Rank Sum Test Results for Column 3 and Column 4:")
print(f"statistic={wilcoxon_ranksums_test.statistic}, p-value={wilcoxon_ranksums_test.pvalue}")
