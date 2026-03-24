import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 20, 18]


plt.plot(x, y, marker='o', linestyle='-', color='pink')

plt.title("Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid(True)

plt.show()
