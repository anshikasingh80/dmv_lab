import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [2, 3, 5, 7, 6, 8, 9]

plt.scatter(x, y, color='pink', edgecolor='black', s=100) 

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot")

plt.grid(True)

plt.show()
