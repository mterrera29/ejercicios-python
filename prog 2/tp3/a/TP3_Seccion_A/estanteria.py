#Ejercicio 3
class Estanteria:
    
    numero_siguiente = 1
    
    def __init__(self):
        self.__cajas = []
        #Ejercicio 5
        self.__numero = Estanteria.numero_siguiente
        Estanteria.numero_siguiente = Estanteria.numero_siguiente + 1
        
    def agregar_caja(self, caja):
        self.__cajas.append(caja)
        
    def remover_caja(self, caja):
        self.__cajas.remove(caja)
        
    def obtener_numero(self):
        return self.__numero
    
    def obtener_cajas(self):
        return self.__cajas
    
    #Ejercicio 6
    def __str__(self):
        cajas = ",".join(str(caja) for caja in self.__cajas)
        return f'N° {self.__numero}. Cajas: {cajas}'
    
    def __eq__(self, other):
        if (isinstance(other, Estanteria)):
            return other.__numero == self.__numero
        return NotImplemented
    
    