class Corcho:
    def __init__(self, Bodega):
        self.Bodega=Bodega
    
    def __str__(self):
        return self.Bodega

class Botella:
    def __init__(self, Corcho:Corcho):
        self.CorchoDeBotella=Corcho

class Sacacorcho:
    def __init__(self):
        self.CorchoSacacorcho=None
    
    def Destapar(self,Botella:Botella):
        if self.CorchoSacacorcho==None:
            if Botella.CorchoDeBotella!=None:
                self.CorchoSacacorcho=Botella.CorchoDeBotella
                Botella.CorchoDeBotella=None
                print("Botella destapada")
            else:
                print("La botella ya esta destapada")
        else:
            print("El sacacorchos ya tiene un corcho, primero hay que limpiarlo")
            
    def Limpiar(self):
        if self.CorchoSacacorcho==None:
            print("El sacacorchos ya esta limpio")
        else:
            self.CorchoSacacorcho=None
            print("Sacacorcho limpiado")

Corcho1=Corcho("Latitud 44")
Botella1=Botella(Corcho1)
Sacacorcho1=Sacacorcho()

Sacacorcho1.Destapar(Botella1)