#Ejercicio 2
class Caja:
    
    numero_siguiente = 1
    
    def __init__(self, alto, ancho, profundidad, material):
        self.__alto = alto
        self.__ancho = ancho
        self.__profundidad = profundidad
        self.__material = material
        self.__items = []
        #Ejercicio 5
        self.__numero = Caja.numero_siguiente
        Caja.numero_siguiente = Caja.numero_siguiente + 1
        
    def establecer_alto(self, alto):
        self.__alto = alto
        
    def establecer_ancho(self, ancho):
        self.__ancho = ancho
        
    def establecer_profundidad(self, profundidad):
        self.__profundidad = profundidad
        
    def establecer_material(self, material):
        self.__material = material
        
    def agregar_item(self, item):
        self.__items.append(item)
        
    def remover_item(self, item):
        self.__items.remove(item)
        
    def obtener_numero(self):
        return self.__numero

    def obtener_dimensiones(self):
        return f'Alto: {self.__alto}. Ancho: {self.__ancho}. Profundidad: {self.__profundidad}'
    
    def obtener_items(self):
        return self.__items
    
    def obtener_material(self):
        return self.__material
    
    #Ejercicio 6
    def __str__(self):
        items = ",".join(str(item) for item in self.__items)
        return f'Caja N°: {self.__numero}. Dimensiones: {self.obtener_dimensiones()}. Material: {self.__material}. Items: {items}'
    
    def __eq__(self, other):
        if (isinstance(other, Caja)):
            return other.__numero == self.__numero
        return NotImplemented
    
        