import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 5, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = y1*y2

plt.title(label='sin&cos', loc='center')
plt.plot(x, y1, label='sin', color='r', linewidth=3)
plt.plot(x, y2, label='cos', c='g', linewidth=4)
plt.scatter(x, y3, label='mul', c='b', linewidths=2, marker='+')
plt.legend(loc='upper right')
plt.grid(linestyle='-.', color='c', linewidth=1)

plt.show()