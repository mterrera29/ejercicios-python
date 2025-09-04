from cancion import *

cancion1 = Cancion("Adios",350,"rock")
cancion2 = Cancion("Crimen",250,"rock")
cancion3 = Cancion("Primavera 0",410,"rock")

print(cancion1.obtenerGenero())
print(cancion2.obtenerGenero())
print(cancion3.obtenerGenero())

cancion2.establecerGenero("bolero")

print(cancion2.obtenerGenero())

from circulo import *

circulo1 = Circulo(2.0)
circulo2 = Circulo(5.6)
circulo3 = Circulo(7.8)

print(circulo1.PI)
print(circulo2.PI)
print(circulo3.PI)

circulo4 = Circulo(7.2)
circulo5 = Circulo(7.2)

print(circulo4==circulo5)
print(circulo4.obtenerPerimetro( )== circulo5.obtenerPerimetro())
