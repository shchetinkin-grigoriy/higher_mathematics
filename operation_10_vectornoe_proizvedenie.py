# %matplotlib inline
import numpy as np                  #для работы с массивами - их по умолчанию в Python нет
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D     #об

#0 Инициализация отображения в 3D
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.grid(True)

#1 Векторное произведение
X, Y, Z = np.array([0, 0, 0], float), np.array([0, 0, 0], float), np.array([0, 0, 0], float)
a = np.array([1, 0, 0], float)
b = np.array([0, 1, 0], float)
c = np.cross(a, b)               #векторное произведение
print(c)

U, V, W = np.array([a[0], b[0], c[0]], float), np.array([a[1], b[1], c[1]], float), np.array([a[2], b[2], c[2]], float)

fig = plt.figure();
# ax = fig.add_subplot(111)
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, U, V, W)
ax.set_xlim([0, 5])
ax.set_ylim([0, 5])
ax.set_zlim([-2, 2])

plt.show()
