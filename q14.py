import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a random dataset of 600 rows and 15 columns.
np.random.seed(42)  # For reproducibility
dataset = pd.DataFrame(np.random.randint(-100, 101, size=(600, 15)), columns=[f'col{i}' for i in range(1, 16)])

# Step 2: Plot scatter graph between Column 5 and Column 6.
plt.scatter(dataset['col5'], dataset['col6'])
plt.xlabel('Column 5')
plt.ylabel('Column 6')
plt.title('Scatter Plot: Column 5 vs. Column 6')
plt.show()

# Step 3: Plot histogram of each column in a single graph.
dataset.hist(figsize=(12, 10), bins=20)
plt.suptitle('Histogram of Each Column', fontsize=16)
plt.show()

# Step 4: Plot the Box plot of each column in a single graph.
dataset.plot(kind='box', vert=False, figsize=(12, 6))
plt.title('Box Plot of Each Column')
plt.xlabel('Values')
plt.show()
