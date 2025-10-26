from naveEspacial import *

""" 12
class VideoJuego():
  nave1 = NaveEspacial("‘V’",1000)
  nave2 = nave1
  nave3 = NaveEspacial("‘V’",1000)
  b1 = nave1 == nave2
  b2 = nave1 == nave3
  nave2.establecerCombustible(800)
  print(nave1.obtenerCombustible()) """
  
nave_espacial1 = NaveEspacial('R', 500)
nave_espacial2 = NaveEspacial('R', 500)
print('Nave 1 = Nave 2: ' + str(nave_espacial1 == nave_espacial2))