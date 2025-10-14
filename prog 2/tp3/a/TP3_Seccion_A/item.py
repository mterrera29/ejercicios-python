#Ejercicio 1
class Item:
    
    numero_siguiente = 1
    
    def __init__(self, descripcion):
        self.__descripcion = descripcion
        #Ejercicio 5
        self.__numero = Item.numero_siguiente
        Item.numero_siguiente = Item.numero_siguiente + 1
        
    def obtener_numero(self):
        return self.__numero
    
    def obtener_descripcion(self):
        return self.__descripcion
    
    #Ejercicio 6
    def __str__(self):
        return f'N°: {self.__numero}. Descripcion: {self.__descripcion}'
    
    def __eq__(self, other):
        if (isinstance(other,Item)):
            return other.__numero == self.__numero
        return NotImplemented
        