# 2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina.
# La clase debe contener como miembros:
#  Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
#  Un atributo para el estado (lleno o vacío).
#  Un atributo n, que indica la cantidad máxima de cebadas.

# Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
# excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!

# Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
# debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!


# Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
# de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
# “Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.

class Mate:

    def __init__(self):
        self.Estado="Vacio"
        self.cantidadMaximas=10
        self.CebadasRestantes=self.cantidadMaximas

    def cebar(self):
        if self.Estado == "Lleno":
            print("¡Cuidado! ¡Te quemaste!")
        else:
            self.Estado="Lleno"
    def beber(self):
        if self.Estado == "Vacio":
            print("¡El mate está vacio!")
        else:
            self.Estado="Vacio"
            if self.CebadasRestantes == 0:
                print("Advertemcia: el mate está lavado \n Puede serguir tomando el mate pero recomendamos Cambiar la yerba")
            else:
                self.CebadasRestantes-=1
    def CambiarYerba(self):
            self.cantidadMaximas=10
            self.CebadasRestantes=self.cantidadMaximas

UnLeoMatioli1=Mate
respuestaUsuario=None
while respuestaUsuario!="Dejar de tomar":
    respuestaUsuario=input("Que accion desea realizar? \n ¿Cebar, Beber o Cambiar la yerba?" )
    if respuestaUsuario == "Cebar":
        UnLeoMatioli1.cebar()
    elif respuestaUsuario == "Beber":
        UnLeoMatioli1.beber()
    elif respuestaUsuario == "Cambiar la yerba":
        UnLeoMatioli1.CambiarYerba()
    elif respuestaUsuario != "Dejar de tomar":
        print("No se puede realizar esa accion, vuelva intentar por favor")