#1)Escriba una función que muestre todos los números primos entre 1 y un número n que es
#ingresado por parámetro.

"""
def numeros_primos(numero):
    primos = []
    for num in range(1, numero+1):
        es_primo = True
        for i in range(2, num):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(num)
    return primos

numero=int(input("Hasta que numero desea corroborar?"))
print(numeros_primos(numero))
"""

#2) Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta
#que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje
#avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del
#programa de acuerdo a estos criterios:
#• Use un test condicional en el ciclo while para detener la ejecución.
#• Use un test condicional dentro del ciclo para decidir si continuar la ejecución. 

# Tes condicional While

"""
def hacer_sandwich():
    condimento = ""
    condimentos= []
    while condimento != "salir":
        condimento = input("Ingrese un condimento para su sándwich (o 'salir' para terminar): ")
        if condimento != "salir":
            condimentos.append(condimento)
            print(f"Se ha agregado {condimento} a su sándwich.")
    print(f"Su sándwich está listo. Los condimentos son {condimentos}")
hacer_sandwich()
"""

"""
# Test condicional dentro del ciclo
def hacer_sandwich():
    continuar = True
    condimentos=[]
    while continuar:
        condimento = input("Ingrese un condimento para su sándwich (o 'salir' para terminar): ")
        if condimento == "salir":
            continuar = False
        else:
            print(f"Se ha agregado {condimento} a su sándwich.")
            condimentos.append(condimento)
    print(f"Su sándwich está listo. Los condimentos son {condimentos}")
hacer_sandwich()

"""

#3)
#A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un 
#tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje 
#describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez 
#usando argumentos por posición. Llámela una segunda vez usando argumentos por clave.
 
#B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por 
#defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los 
#valores por defecto, y la segunda con valores diferentes. 

#A-)

"""
def hacer_remera(Tamaño,Mensaje):
    print(f"El tamaño de la remera será {Tamaño} y el mensaje será {Mensaje}")

hacer_remera((input("Insertar tamaño ")),(input("Insertar mensaje ")))
hacer_remera(Mensaje=input("insertar mensaje "),Tamaño=input("Insertar tamaño "))
"""

#B-)

"""
def hacer_remera(Tamaño="L",Mensaje="Me gusta python"):
    print(f"El tamaño de la remera será {Tamaño} y el mensaje será {Mensaje}")

while True:
    hacer_remera()
    if input("Desea alterar la remera?") == "Si":
        hacer_remera(input("Que tamaño será? "),input("Que mensaje tendrá"))
    if input("Hará otra remera?") == "No":
        break
"""

#4) Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros 
#de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo 
#número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …). 

"""
def Fibonacci(Vueltas):
    fib = [0, 1] 
    while len(fib) < Vueltas:
        fib.append(fib[-1] + fib[-2])
    return fib
Vueltas=int(input("Cuantos numeros quiere que se devuelva?"))
print(Fibonacci(Vueltas))
"""

#5) (Opcional) Calculadora más inteligente: Modifique el ejercicio 9 del primer practico para que 
#la calculadora sea capaz de devolver el resultado solamente de una operación especificada por 
#el usuario. Por ejemplo, si el usuario ingresa dos numeros x, y, y luego ingresa ‘1’, la 
#calculadora devuelve la suma entre los numeros x,y; si ingresa ‘2’, devuelve la resta, etc.

"""
def Suma(a,b):
    print(a+b)
def Resta(a,b):
    print(a-b)
def Multiplicacion(a,b):
    print(a*b)
def division(a,b):
    print(a/b)



while input("Desea hacer algun calculo?") == "Si":
    a= int(input("introduzca su primer numero"))
    b= int(input("introduzca su segundo numero"))
    respuesta=int(input("Presione 1 en caso de suma \n presione 2 en caso de resta \n presione 3 en caso de multiplicacion \n presione 4 en caso de division"))
    while respuesta >4:
        print("No hay accion accion asociada a este numero, elija otro por favor")
        respuesta=int(input("Presione 1 en caso de suma \n presione 2 en caso de resta \n presione 3 en caso de multiplicacion \n presione 4 en caso de division"))
    if respuesta == 1:
        Suma(a,b)
    elif respuesta == 2:
        Resta(a,b)
    elif respuesta == 3:
        Multiplicacion(a,b)
    elif respuesta == 4:
        division(a,b)
"""

#6) (Opcional) Conversión imperial: Desarrollar un programa en Python que pueda convertir 
#gramos a libras, centímetros a pulgadas y kilómetros a millas. El programa debe permitir la 
#conversión en ambos sentidos. 
# 1.60934 Km = 1 milla 
# 0.393701 pulgadas = 1 cm 
# 0.00220462 libras = 1 gramo 

"""
def Kg_a_Libra(Valor):
    print(f"La conversion de {Valor} a Libras es de: "+Valor*2.20462)
def Libra_a_kg(Valor):
    print(f"La conversion de {Valor} a Kilogramos es de: "+Valor/2.20462)
def Pulgada_a_Centimetro(Valor):
    print(f"La conversion de {Valor} centimetros a pulgadas es de:"+Valor/2.54)
def Centimetro_a_Pulgada(Valor):                                                    #Dato: usé la formula simplificada de la pulgada, 2,54cm por pulgada 
    print(f"La conversion de {Valor} pulgadas a centimetros es de:"+Valor*2.54)
def Kilometro_a_Milla(Valor):
    print(f"La conversion de {Valor} kilometros a millas es de:"+Valor/1.60934)
def Milla_a_Kilometro(Valor):
    print(f"La conversion de {Valor} Millas a kilometros  es de:"+Valor*1.60934)

Respuesta=input("Que desea realizar? Convertir a: \n Libras \n Kilogramos \n Pulgadas \n Centimetros \n Millas \n Kilometros")
Valor=float(input("Inserte su valor"))
if Respuesta == "Libra":
    Libra_a_kg(Valor)
elif Respuesta == "Kilogramos":
    Kg_a_Libra(Valor)
elif Respuesta == "Pulgadas":
    Centimetro_a_Pulgada(Valor)
elif Respuesta == "Centimetros":
    Pulgada_a_Centimetro(Valor)
elif Respuesta == "Millas":
    Kilometro_a_Milla(Valor)
elif Respuesta == "Kilometros":
    Milla_a_Kilometro(Valor)

"""