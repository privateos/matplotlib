import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 5, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = y1 - y2

plt.title(label='sin&cos', loc='center')
plt.scatter(x, y1, label='sin', color='r', linewidths=1, marker='+')
plt.scatter(x, y2, label='cos', c='g', linewidths=0.1, marker='o')
plt.scatter(x, y3, label='diff', c='b', linewidths=2, marker='d')
plt.legend(loc='upper right')
plt.show()