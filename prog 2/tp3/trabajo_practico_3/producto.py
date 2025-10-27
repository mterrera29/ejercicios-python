# Ejercicio 1

class Producto():
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def obtener_nombre(self):
        return self.__nombre


    # Ejercicio 8
    def __str__(self):
            return self.__nombre

    def __eq__(self, other):
        if isinstance(other, Producto):
            return other.__nombre == self.__nombre
        return NotImplemented