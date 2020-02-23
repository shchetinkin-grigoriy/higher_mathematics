# import matplotlib as matplotlib
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
a=6
b=2
x = np.linspace(-a, a, 201)
y_elipse = b * np.sqrt(1 - (x ** 2)/(a ** 2))

plt.xlim(-a, a)
plt.ylim(-a, a)
plt.plot(x, y_elipse, color='blue')
plt.plot(x, -y_elipse, color='blue')
plt.show()



# x = np.linspace(-1, 3, 201)
# print(np.poly([1, 1, 2]))
# plt.plot(x, x**3-4*x**2+5*x-2)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.ylim(-2,2)
# plt.show()
# print(np.roots([ 1., -4.,  5., -2.]))
#
