#8. (Opcional) Escriba una función que pida al usuario ingresar su fecha de
#nacimiento y sea capaz de devolver la cantidad de días desde su
#nacimiento hasta hoy.

import datetime

def dias_desde_nacimiento():
    dia = int(input("Ingrese el día de su fecha de nacimiento: "))
    mes = int(input("Ingrese el mes de su fecha de nacimiento: "))
    año = int(input("Ingrese el año de su fecha de nacimiento: "))
    fecha_nacimiento = datetime.datetime(año, mes, dia)
    hoy = datetime.datetime.now()
    diferencia = hoy - fecha_nacimiento
    diastranscurridos = diferencia.days
    return diastranscurridos
