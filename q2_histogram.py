import matplotlib.pyplot as plt

data = [12, 15, 14, 10, 18, 20, 22, 19, 15, 13, 
        17, 21, 25, 30, 28, 24, 23, 26, 27, 29]

plt.figure(figsize=(8, 5))
plt.hist(data, bins=5, color='pink', edgecolor='black')

plt.title("Histogram Example")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
