import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
values = [25, 30, 20, 25]

colors = ['pink', 'lightpink', 'hotpink', 'deeppink']

fig, ax = plt.subplots()

def animate(i):
    ax.clear()
    new_values = np.array(values) + np.random.randint(-5, 6, size=len(values))
    new_values = np.clip(new_values, 0, None)  
    ax.pie(new_values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.set_title("Dynamic Pie Chart")

ani = animation.FuncAnimation(fig, animate, frames=20, interval=800)

plt.show()
