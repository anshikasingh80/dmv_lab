import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 15, 7, 12, 9]

plt.bar(categories, values, color='pink', edgecolor='black')

plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Static Bar Chart")

plt.show()
