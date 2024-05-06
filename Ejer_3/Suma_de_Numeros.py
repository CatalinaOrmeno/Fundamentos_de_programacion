#Crea una lista de números enteros.
nums = [1, 50, 878, 64, 2, 4, 5, 6, 1]
suma_ = 0
  
#Utiliza un bucle for para recorrer la lista y calcular la suma total de los elementos.
for ind in range(len(nums)):
    print(f'{ind + 1}. {nums[ind]}')
    suma_ = int(suma_ + nums[ind])

#Muestra el resultado final en la salida.
print(suma_)

