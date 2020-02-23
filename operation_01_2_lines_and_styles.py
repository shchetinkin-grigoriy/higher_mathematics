# %matplotlib inline
import numpy as np                  #для работы с массивами - их по умолчанию в Python нет

import matplotlib.pyplot as plt     #для генерации графиков

#1 Расширенная работа
x = np.linspace(-1, 1, 201)
plt.plot(x, np.arcsin(x))
plt.plot(x, np.arccos(x))
plt.plot(x, np.arctan(x))
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-1,1)
plt.ylim(-np.pi,np.pi)

#указание стилей и построение прямых
plt.plot([-1,1],[-np.pi/2,-np.pi/2], color ='blue', linewidth=0.75, linestyle ="--")
plt.plot([-1,1],[0,0], color ='red', linewidth=0.75, linestyle ="--")
plt.plot([-1,1],[np.pi/2,np.pi/2], color ='blue', linewidth=0.75, linestyle ="--")

plt.grid(True)
plt.show()
