# import matplotlib as matplotlib
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

k = 1
x = np.linspace(-np.pi, np.pi, 201)
plt.grid(True)
plt.plot(x, k*np.sin(x))
k = 5
plt.plot(x, k*np.sin(x))
plt.xlabel('x')
plt.ylabel('y')
plt.axis('tight')
plt.show()
