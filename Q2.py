import numpy as np
import matplotlib.pyplot as plt

x, y = np.random.multivariate_normal([0, 0],[[1, 0], [0, 1]], 2000).T
plt.plot(x, y, 'x')
plt.axis('equal')
plt.show()
