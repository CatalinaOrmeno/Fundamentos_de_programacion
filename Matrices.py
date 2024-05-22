import numpy as np

#arange
#ones
#zeros
#empty
#linspace


array = np.array(range(10))
print(array)
print('Dimenciones:', array.ndim)
print('Tamaño:', array.size)
print('Forma:', array.shape,'\n')

print(array[0])
print(array[0:5])
print(array[0:10:2])
print(array[-1])
print(array[::-1])

array2 = np.arange(10, 21, 2, 'int8')
print(array2)

array3 = np.linspace(1, 10, 3)
print(array3)

array4 = np.array([[1, 2, 3],[4, 5, 6]])
print(array4)
print('Dimenciones:', array4.ndim)
print('Tamaño:', array4.size)
print('Forma:', array4.shape)

array5 = np.arange(27).reshape(3,3,3)
print(array5)
print('Dimenciones:', array5.ndim)
print('Tamaño:', array5.size)
print('Forma:', array5.shape)

array6 = np.arange(1,101).reshape(10,10)
print(array6)
print('Dimenciones:', array6.ndim)
print('Tamaño:', array6.size)
print('Forma:', array6.shape)

array7 = np.random.randint(1,101,(10,10))
print(array7)
print(array7[0][0])

nuevo =  np.vstack((array6, array7))
print(nuevo)
