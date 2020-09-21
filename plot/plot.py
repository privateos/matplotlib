import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 5, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.title(label='sin&cost', loc='center')
plt.plot(x, y1, linestyle='-', linewidth=2, label='sin', color='r')
plt.plot(x, y2, ls='--', lw=3, label='cos', c='g')
plt.legend(loc='upper right')
plt.show()