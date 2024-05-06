import random

var=random.randint(1,6)

if var==1:
    print(var,'= Fracaso')
elif var==2 or var==3:
    print(var,'= Podría mejorar')
elif var==4 or var==5:
    print(var,'= Bastante bien')
elif var==6:
    print(var,'= Excelente!')

