from cancion import *

cancion1 = Cancion("Adios",350,"rock")
cancion2 = Cancion("Crimen",250,"rock")
cancion3 = Cancion("Primavera 0",410,"rock")

print(cancion1.obtenerGenero())
print(cancion2.obtenerGenero())
print(cancion3.obtenerGenero())

cancion2.establecerGenero("bolero")

print(cancion2.obtenerGenero())