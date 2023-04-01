#1. Escriba una función redondear() que permita redondear un número
#decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
#entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
#anterior (3).

import math
def Redondear(numero):
    if numero > 3.50:
        return math.ceil(numero)
    else:
        return math.floor(numero)
