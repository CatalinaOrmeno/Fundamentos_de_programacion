import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1)
print(array2)

array1 = array1[:, np.newaxis]
array2 = array2[:, np.newaxis]

nuevo = np.hstack((array1, array2))
print(nuevo)