import numpy as np
from matplotlib import pyplot

rng = np.random.RandomState(123)

d = 2
N = 10
mean = 5

x1 = rng.randn(N, d) + np.array([0, 0])
x2 = rng.randn(N, d) + np.array([mean, mean])

print(x1)
print(x2)

x = np.concatenate((x1, x2), axis=0)
print(x)

# pyplot.plot(x1, x2)
# pyplot.show()