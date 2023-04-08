# 7) Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
# Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
# postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
# muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método.

from tp6_6 import Usuario

class Admin(Usuario):
    def __init__(self, nombre, apellido, nickname,privilegios):
        super().__init__(nombre, apellido, nickname, direccion="No hay un correo vinculado a esta cuenta")
        self.privilegios=["Postear en el foro","Borrar un post"]
        self.privilegios.append(privilegios)
    def Mostrar_Privilegios(self):
        print(f"El usuario {self.nickname} tiene los siguientes privilegios:")
        print(self.privilegios)
    
def Cuerpo_Del_Codigo():
    Administrador=Admin("Mateo","Marquez","FukoHoe","Banear usuarios")
    Administrador.Mostrar_Privilegios()

if __name__ == "__main__":
    Cuerpo_Del_Codigo()