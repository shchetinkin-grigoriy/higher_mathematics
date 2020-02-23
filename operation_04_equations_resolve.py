# %matplotlib inline
import numpy as np                  #для работы с массивами - их по умолчанию в Python нет

import matplotlib.pyplot as plt     #для генерации графиков

#Решение уравнений
from scipy.optimize import fsolve   #функция поиска решений

#1 Определение графика

x = np.linspace(-2, 3, 201)
plt.plot(x, (np.exp(x) - 1) / x)
plt.plot(x, x ** 2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-1, 5)
plt.grid(True)
plt.show()


#2 Определение функции и поиск решения
def equations(p):
    x, y = p
    #возвразщает решение близкое, если оно близко к 0 кортежа сравнения функций
    return (y - x ** 2 + 1, np.exp(x) - x * y - 1)

#вызывается функция и выводится результат только если она возвразщает решение близкое к 0 кортежа сравнения функций
x1, y1 = fsolve(equations, (-2, 1))
# x1, y1 =  fsolve(equations, (-2, 1))

print(x1, y1)