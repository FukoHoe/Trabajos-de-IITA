#7. (Opcional) Sorteo: Escriba un programa que simule un sorteo donde
#toman uno o más papeles al azar de un pozo para elegir los ganadores.

import random
def tomarDelPozo(ListaParticipantes): 
    PosicionGanadora=random.randrange(1,len(ListaParticipantes)+1)
    if PosicionGanadora in PosicionesOcupadas:
        tomarDelPozo(ListaParticipantes)
    PosicionesOcupadas.append(PosicionGanadora)
    Ganador=ListaParticipantes[PosicionGanadora]
    return Ganador
ListaParticipantes=["Vacio"]
PosicionesOcupadas=[]
while True: 
    if input("Desea añadir otro participante? en caso de que no escriba No ") !="No":
        ListaParticipantes.append(input("Ingrese su nombre"))
    else:
        break
cantidadDeGanadores=int(input("Cuantos ganadores deberá haber?"))
if cantidadDeGanadores<=len(ListaParticipantes):
    for i in range(cantidadDeGanadores):
        print(tomarDelPozo(ListaParticipantes))

