# %matplotlib inline
import numpy as np                  #для работы с массивами - их по умолчанию в Python нет

import matplotlib.pyplot as plt     #для генерации графиков
import itertools

#1 Random funcs
for i in range(0, 5):
    x = np.random.uniform(0, 10)
    print("орел" if x<5 else "решка")

#
k, n = 0, 10000
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
x = a + b
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
print(k, n, k/n)

#2 Комбинаторика
for p in itertools.product("01",repeat=3):
    print(''.join(p))

for p in itertools.permutations("0123",2):
    print(''.join(str(x) for x in p))

for p in itertools.combinations("0123", 2):
    print(''.join(p))

#3 Histogram
x = np.random.rand(1000)
num_bins = 5
n, bins, patches = plt.hist(x, num_bins)
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()

