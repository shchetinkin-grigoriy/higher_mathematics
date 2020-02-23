# %matplotlib inline
from matplotlib import pylab

# you can now use both pyplot and numpy
# functions as if they had been imported

# from numpy namespace
x = pylab.linspace(0,10,9)

# from numpy.random namespace
y = pylab.randn(9)

# from pyplot namespace
pylab.scatter(x,y)
pylab.show()
