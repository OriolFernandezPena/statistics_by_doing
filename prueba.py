import numpy as np


x = np.random.poisson(size=100000)

print(x.mean(), x.std())