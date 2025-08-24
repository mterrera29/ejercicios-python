from naveEspacial import *
from pelota import *


pelota1 = PelotaConNombre('Pelota 1')
pelota2 = PelotaConNombre('Pelota 2')
pelota1.establecerNombre('Pelota 2')
pelota2.establecerNombre('Pelota 1')
print(pelota1.obtenerNombre())
print(pelota2.obtenerNombre())