# 1) Escribir una clase llamada Rectángulo que contenga una base y 
# una altura, y que contenga un método que devuelva el área
# del rectángulo.

class rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def devolverArea(self):
        return (self.base*2)+(self.altura*2)

base=int(input("Introduzca la base del rectangulo "))
altura=int(input("Introduzca la altura del rectangulo "))
rectangulo1=rectangulo(base,altura)
print(rectangulo1.devolverArea())