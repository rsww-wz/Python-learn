import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6])
y = 2 * x

plt.figure(num='first')
plt.bar(x, y, color='red', alpha=0.6, width=0.3)
plt.show()

plt.figure(num='second')
plt.bar(x, y, color='red', alpha=0.6, width=0.3)
plt.bar(x + 0.3, x * 3, color='blue', alpha=0.6, width=0.3)
plt.show()
