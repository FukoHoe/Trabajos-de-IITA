# 4) Una heladeria es un tipo especial de restaurante. Cree una clase Restaurante, cuyo metodo __init__() guarde dos atributos:
# restaurante_nombre y tipo_comida. 
# Cree un metodo describir_restaurante() que muestre estas piezas de informacien, y un metodo
# abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora este abierto.

# Luego cree una clase Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado 
# sabores que almacene una lista de los sabores de helado disponibles. 
# Escriba tambien un metodo que muestre estos valores, cree una instancia de la clase y llame al metodo.

class Restaurante:

    def __init__(self,Nombre,TipoComida):
        self.Nombre=Nombre
        self.TipoComida=TipoComida
    
    def describir_restaurante(self):
        print("El nombre del restaurante es: ",self.Nombre)
        print("El tipo de comida que se vende es: ",self.TipoComida)
    
    def abrir_restaurante(self):
        print(f"El <{self.Nombre}> esta abierto")

class Heladeria(Restaurante):
     
    def __init__(self, nombre, TipoComida="Helados"):
        super().__init__(nombre,TipoComida="Helados")
        self.Sabores=[]

    def AnadirSabor(self,Sabores):
        self.Sabores.append(Sabores)

    def MostrarDatos(self):
        print("El nombre del restaurant es:",self.Nombre)
        print("El tipo de comida que venden es:",self.TipoComida)
        print("La lista de sabores disponible es:")
        for sabor in self.Sabores:
            print("- " + sabor)

def Cuerpo_Del_Codigo():
    Nombre_Restaurante1=input("Como se llama su local? ")
    Heladeria1=Heladeria(Nombre_Restaurante1)
    respuesta=None
    while respuesta != "Salir":
        respuesta=input("Que  accion desea realizar? Anadir Sabor, Mostrar Datos o Salir ")
        if respuesta == "Anadir Sabor":
            Sabor=input("Que sabor desea anadir?")
            Heladeria1.AnadirSabor(Sabor)
            print("Se ha añadido un nuevo sabor al catalogo")
        elif respuesta == "Mostrar Datos":
            Heladeria1.MostrarDatos()
    

if __name__ == "__main__":
    Cuerpo_Del_Codigo()

