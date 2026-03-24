import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o', color='pink')

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("XY Plot")

plt.grid(True)

plt.show()
