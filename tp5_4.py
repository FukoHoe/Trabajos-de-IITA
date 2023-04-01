#4. Escriba un programa que devuelva un número par al azar entre 2 y 10
#(pista: para comprobar si se pueden generar todos los números, pruebe
#ejecutar el programa dentro de un ciclo infinito).

import random
def generarazar(inicio=2, Fin=10):
    return random.randint(inicio, Fin)

"""
while True:
    print (generarazar())               #Prueba del modulo
"""