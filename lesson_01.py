# import matplotlib as matplotlib
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

print('#3-3: Перевод в полярные координаты и рисование круга: ')
x = np.linspace(-3, 3, 201)
y = np.sqrt(3**2 - x ** 2)
def convert_to_polar(func, x, y):
    return func(x, y), np.arctan(x/y)
r, a = convert_to_polar(lambda x,y: np.sqrt(x ** 2 + y ** 2), x, y)
plt.plot(x, y, color='blue')
plt.plot(x, -y, color='blue')
plt.show()
