# 5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, 
# y los métodos recibir_ataque, que reduzca la vida según una cantidad recibida y
# lance una excepción si la vida pasa a ser menor o igual que cero,
# y mover que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.

class Personaje:
    def __init__(self):
        self.vida=100
        self.posicionIzq=0
        self.posicionDer=0
        self.posicionArriba=0
        self.posicionAbajo=0
        self.velocidad=3

    def recibir_ataque(self,dañoRecibido):
        if self.vida>0:
            self.vida-=dañoRecibido
            if self.vida<=0:
                print("Ya no tienes mas puntos de vida")
        else:
            print("No tienes mas puntos de vida")
    def mover(self,direccion):
            if direccion=="Izquierda":
                self.posicionIzq+=self.velocidad
            elif direccion=="Derecha":
                self.posicionDer+=self.velocidad
            elif direccion=="Arriba":
                self.posicionArriba+=self.velocidad
            elif direccion=="Abajo":
                self.posicionAbajo+=self.velocidad
            else:
                print("No es una direccion valida, elija otra")
                direccion=input("Hacia que direccion quiere dirigirse?")
                mover(direccion)
            
# Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
# personaje, al que le debe hacer el daño indicado por el atributo ataque.

class Soldado(Personaje):
    def __init__(self):
        super().__init__()
        self.ataque=15
    
    def atacar(self,objetivo:Personaje):
        objetivo1=objetivo
        objetivo1.recibir_ataque(self.ataque)

# Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
# devuelva la cantidad cosechada

class Campesino(Personaje):
    def __init__(self):
        super().__init__()
        self.cosecha=10
    def cosechar(self):
        return self.cosecha
    
Personaje1=Personaje()
Soldado1=Soldado()
Campesino1=Campesino()

respuesta=None
while respuesta!="Salir":
    print("Que accion desea realizar? ")
    personajeSelec=input("Elija un personaje \n - Personaje \n - Soldado \n - Campesino \n")
    if personajeSelec == "Personaje":
        accion=input("Que desea realizar? \n mover o salir \n")
        if accion == "Mover":
            direccion=input("Hacia donde se quiere dirigir? \n Izquierda, Derecha \n Arriba o Abajo \n")
            Personaje1.mover(direccion)
    elif personajeSelec == "Soldado":
        accion=input("Que desea realizar? \n Mover, Atacar o Salir \n")
        if accion == "Mover":
            direccion=input("Hacia donde se quiere dirigir? \n Izquierda, Derecha \n Arriba o Abajo \n")
            Soldado1.mover(direccion)
        elif accion == "Atacar":
            objetivo=input("A quien desea atacar? \n Pesonaje o Campesino \n" )
            if objetivo == "Personaje":
                Soldado1.atacar(Personaje1)
            elif objetivo == "Campesino":
                Soldado1.atacar(Campesino1)
            else:
                print("objetivo no encontrado")
    elif personajeSelec == "Campesino":
        accion=input("Que desea realizar? \n mover, Cosechar o salir \n")
        if accion == "Mover":
            direccion=input("Hacia donde se quiere dirigir? \n Izquierda, Derecha \n Arriba o Abajo \n")
            Campesino1.mover(direccion)
        elif accion == "Cosechar":
            print("se ha cosechado", Campesino1.cosechar())
    respuesta=input("Desea realizar otra accion? \n en caso de que no escriba Salir \n")