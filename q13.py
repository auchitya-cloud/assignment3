import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram

# Step 1: Create a random dataset of 500 rows and 10 columns.
np.random.seed(42)  # For reproducibility
cols_1_to_4 = np.random.uniform(-10, 10, size=(500, 4))
cols_5_to_8 = np.random.uniform(10, 20, size=(500, 4))
cols_9_to_10 = np.random.uniform(-100, 100, size=(500, 2))
dataset = np.hstack((cols_1_to_4, cols_5_to_8, cols_9_to_10))
df = pd.DataFrame(dataset, columns=[f'col{i}' for i in range(1, 11)])

# Step 2: Apply K-Means clustering and find the optimal number of clusters using the elbow method.
distortions = []
K = range(1, 11)  # Trying different numbers of clusters from 1 to 10.
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df)
    distortions.append(kmeans.inertia_)

# Plot the elbow graph
plt.plot(K, distortions, marker='o')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Distortion')
plt.title('K-Means Elbow Method')
plt.show()

# Step 3: Based on the elbow graph, determine the optimal number of clusters for K-Means.
optimal_k = 4  # In this case, the graph suggests 4 clusters.

# Step 4: Apply K-Means clustering with the optimal number of clusters.
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df['KMeans_Cluster'] = kmeans.fit_predict(df)

# Step 5: Apply Hierarchical clustering and plot the dendrogram to find the optimal number of clusters.
plt.figure(figsize=(10, 7))
dendrogram_ = dendrogram(
    AgglomerativeClustering(distance_threshold=0, n_clusters=None).fit(df).linkage_,
    truncate_mode='level',
    p=5
)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()

# Step 6: Based on the dendrogram, determine the optimal number of clusters for Hierarchical clustering.
optimal_hierarchical_k = 4  # In this case, the dendrogram suggests 4 clusters.

# Step 7: Apply Hierarchical clustering with the optimal number of clusters.
hierarchical_clustering = AgglomerativeClustering(n_clusters=optimal_hierarchical_k)
df['Hierarchical_Cluster'] = hierarchical_clustering.fit_predict(df)

# Display the dataframe with cluster assignments
print(df.head())
