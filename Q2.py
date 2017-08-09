import numpy as np
import matplotlib.pyplot as plt

list = [1,2,3,4,5]
print type(list)
nparray = np.array(list)
print type(nparray)
array2 = np.array([[1, 2, 3],
		[5, 6, 7],
		[8, 9, 10]])
print "shape of the array is ", array2.shape
print "dimention of the array is ", array2.ndim
array3 = np.arange(0, 9).reshape((3,3))
print array3
print array2
print np.add(array2, array3)
print array2, "*", array3, "=", np.multiply(array2, array3)
x, y = np.random.multivariate_normal([0, 0],[[1, 0], [0, 1]], 2000).T
plt.plot(x, y, 'x')
plt.axis('equal')
plt.show()

