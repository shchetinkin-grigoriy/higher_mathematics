# %matplotlib inline
import numpy as np                  #для работы с массивами - их по умолчанию в Python нет

import matplotlib.pyplot as plt     #для генерации графиков

#1 Полярные координаты
x = np.linspace(0, 15, 100)
y = 8*x
plt.polar(x, y)                     #построение графика в полярных координатах
plt.show()                          # отобраэение