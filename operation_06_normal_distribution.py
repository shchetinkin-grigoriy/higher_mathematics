# %matplotlib inline
import numpy as np                  #для работы с массивами - их по умолчанию в Python нет

import matplotlib.pyplot as plt     #для генерации графиков
from scipy.stats import norm        #для нормально расперделения
import matplotlib.mlab as mlab      #

mu = 50
sigma = 30
x = mu + sigma * np.random.randn(10000)
print(np.mean(x), np.var(x))
num_bins = 20
n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='blue', alpha=0.5)
y = norm.pdf(bins, mu, sigma)
plt.plot(bins, y, 'r--')
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Histogram: $\mu=50$, $\sigma=30$')
plt.subplots_adjust(left=0.15)
plt.show()