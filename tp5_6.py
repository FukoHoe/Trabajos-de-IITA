#6. Encuentre el tiempo de ejecución de los programas de los ejercicios
#anteriores (pista: use el módulo time)

import time

def EmpezarcontarTiempo():
    InicioDelPrograma=time.time()
    return InicioDelPrograma
def TiempoEmpleado(InicioDelPrograma):
     FinDelPrograma=time.time()
     TiempoEmpleado=FinDelPrograma-InicioDelPrograma
     return TiempoEmpleado
