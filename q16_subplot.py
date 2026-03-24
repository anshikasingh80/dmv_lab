import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 2, 5, 4]
y3 = [5, 3, 4, 2, 1]
y4 = [7, 8, 5, 6, 7]

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, y1, marker='o', color='pink')
axs[0, 0].set_title("Line Plot")

axs[0, 1].scatter(x, y2, color='pink', edgecolor='black', s=100)
axs[0, 1].set_title("Scatter Plot")

axs[1, 0].bar(x, y3, color='pink', edgecolor='black')
axs[1, 0].set_title("Bar Chart")

axs[1, 1].pie(y4, labels=x, colors=['pink', 'lightpink', 'hotpink', 'deeppink', 'pink'],
              autopct='%1.1f%%', startangle=90)
axs[1, 1].set_title("Pie Chart")

plt.tight_layout()
plt.show()
