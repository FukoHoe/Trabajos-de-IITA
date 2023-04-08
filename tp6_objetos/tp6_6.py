# 6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
# se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
# usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
# Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno.

class Usuario:
    def __init__(self,nombre,apellido,nickname,direccion="No hay un correo vinculado a esta cuenta"):
        self.nombre=nombre
        self.apellido=apellido
        self.nickname=nickname
        self.direccion=direccion
    def describir_usuario(self):
        print("El nombre de la cuenta es:",self.nickname)
        print(f"La cuenta le pertenece a {self.nombre} {self.apellido}")
        print("El correo vinculado a esta cuenta es:",self.direccion)
    def saludar_usuario(self):
        print(f"Hola {self.nickname} ¿como te encuentras el dia de hoy?")

def Cuerpo_Del_Codigo():
    Usuario1=Usuario("Mateo","Marquez","FukoHoe","CorreoEjemplo@gmail.com")
    Usuario2=Usuario("Tomas","Aisama","FelineBirch","CorreoGenerico@gmail")
    Usuario3=Usuario("Esteban","Hoyos","Zero437","GmaildeEjemplo@gmail.com")
    Usuario4=Usuario("Leonardo","Juarez","HejBok")
    Usuario5=Usuario("Daniel","Han","TheHanChunSeo")

    Usuario1.describir_usuario()
    Usuario1.saludar_usuario()
    
    Usuario2.describir_usuario()
    Usuario2.saludar_usuario()

    Usuario3.describir_usuario()
    Usuario3.saludar_usuario()

    Usuario4.describir_usuario()
    Usuario4.saludar_usuario()

    Usuario5.describir_usuario()    
    Usuario5.saludar_usuario()

if __name__ == "__main__":
    Cuerpo_Del_Codigo()