import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')

circle = plt.Circle((0, 5), 0.5, color='pink')
ax.add_patch(circle)

def update(frame):
    circle.center = (frame, 5) 
    return circle,

animation = FuncAnimation(
    fig,
    update,
    frames=np.linspace(0, 10, 200),
    interval=20,
    blit=True
)

plt.title("Moving Animated Circle")
plt.grid()
plt.show()
