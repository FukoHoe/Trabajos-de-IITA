#5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
#para la adivinación o para buscar consejo. Su mecanismo es muy simple:
#ante una pregunta del usuario, la bola responde con una de 8 posibles
#respuestas:
#- Es seguro que sí
#- Las chances son buenas
#- Puedes contar con ello
#- Pregúntame de nuevo más tarde
#- Concéntrate y pregunta de nuevo
#- No veo con claridad, intenta de nuevo
#- Mi respuesta es no
#- Mis fuentes me dicen que no
#Escriba una función en Python para simular la bola mágica.

import tp5_4

def bolamagica():
    respuesta=tp5_4.generarazar(1,8)
    if respuesta==1:
        print("Es seguro que si")
    elif respuesta==2:
        print("Las chances son buenas")
    elif respuesta==3:
        print("Puedes contar con ello")
    elif respuesta==4:
        print("Preguntame de nuevo mas tarde")
    elif respuesta==5:
        print("Concentrate y pregunta de nuevo")
    elif respuesta==6:
        print("No veo con claridad, intenta de nuevo")
    elif respuesta==7:
        print("Mi respuesta es no")
    elif respuesta==8:
        print("Mis fuentes dicen que no")