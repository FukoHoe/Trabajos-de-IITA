#2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un
#módulo que esté fuera de ese paquete, cree una función de suma de
#decimales que redondee el resultado haciendo uso de la función
#redondear() del paquete recién creado.

from tp5_1 import Redondear
def SumaDeDecimales(Valor1,Valor2):
    resultado=valor1+valor2
    return Redondear(resultado)

"""
valor1=3.4
valor2=4.2                                          # Prueba del modulo
print(SumaDeDecimales(valor1,valor2))
"""