# 8) Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista 
# de strings con los privilegios de manera similar a la del ejercicio 7.
# Mueva el método mostrar_privilegios() de ese ejercicio a esta clase, y haga que una instancia de esta clase 
# sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use el método para mostrar privilegios.

class Privilegios:
    def __init__(self, privilegios=["Postear en el foro", "Banear Usuarios", "Borrar posts"]):
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        print(f"El usuario tiene los siguientes privilegios:")
        for privilegio in self.privilegios:
            print("- " + privilegio)

class Admin:
    def __init__(self, nombre, apellido, nickname, privilegios):
        self.nombre = nombre
        self.apellido = apellido
        self.nickname = nickname
        self.privilegios = privilegios

def Cuerpo_Del_Codigo():
    privilegios1 = Privilegios()
    Administrador1 = Admin("Mateo", "Marquez", "FukoHoe", privilegios1)
    Administrador1.privilegios.mostrar_privilegios() 

if __name__ == "__main__":
    Cuerpo_Del_Codigo()