import matplotlib.pyplot as plt
import numpy as np

# Cluster 1 (positive correlation)
x1 = np.array([1, 2, 3, 4, 5])
y1 = np.array([2, 4, 5, 4, 5])

# Cluster 2 (another cluster, still trending upward)
x2 = np.array([8, 9, 10, 11, 12])
y2 = np.array([10, 12, 13, 12, 14])

# Outliers
x_out = np.array([3, 11])
y_out = np.array([12, 2])

# Combine all data
plt.scatter(x1, y1, color='blue', label='Cluster 1')
plt.scatter(x2, y2, color='green', label='Cluster 2')
plt.scatter(x_out, y_out, color='red', label='Outliers')

# Labels and title
plt.title("Scatter Plot with Clusters, Outliers & Positive Correlation")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()

plt.show()