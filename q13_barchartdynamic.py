import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 15, 7, 12, 9]

fig, ax = plt.subplots()
bars = ax.bar(categories, values, color='pink', edgecolor='black')
ax.set_ylim(0, 20) 

def animate(i):
    new_values = np.array(values) + np.random.randint(-2, 3, size=len(values))
    for bar, val in zip(bars, new_values):
        bar.set_height(val)
    return bars

ani = animation.FuncAnimation(fig, animate, frames=20, interval=500, blit=False)

plt.title("Dynamic Bar Chart")
plt.show()
