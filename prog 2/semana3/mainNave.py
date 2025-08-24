from naveEspacial import *

nave_espacial1 = NaveEspacial('R', 500)
print('Combustible de Nave 1: ' + str(nave_espacial1.obtenerCombustible()))
nave_espacial1.establecerEstadoAlertas(True)
nave_espacial1.agregarCombustible(700)
print('Combustible de Nave 1: ' + str(nave_espacial1.obtenerCombustible()))

nave_espacial2 = NaveEspacial ('A', 0)
print('Combustible de Nave 2: ' + str(nave_espacial2.obtenerCombustible()))
nave_espacial2.establecerEstadoAlertas
nave_espacial2.agregarCombustible(200)
print('Combustible de Nave 2: ' + str(nave_espacial2.obtenerCombustible()))