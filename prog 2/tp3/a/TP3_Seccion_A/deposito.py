#Ejercicio 4
class Deposito:
    
    numero_siguiente = 1
    
    def __init__(self):
        self.__estanterias = []
        #Ejercicio 5
        self.__numero = Deposito.numero_siguiente
        Deposito.numero_siguiente = Deposito.numero_siguiente + 1
        
    def agregar_estanteria(self, estanteria):
        self.__estanterias.append(estanteria)
        
    def remover_estanteria(self, estanteria):
        self.__estanterias.remove(estanteria)
        
    def obtener_numero(self):
        return self.__numero
    
    def obtener_estanterias(self):
        return self.__estanterias
    
    #Ejercicio 6
    def __str__(self):
        estanterias = ",".join(str(estanteria) for estanteria in self.__estanterias)
        return f'Deposito N° {self.__numero}. Estanterias: {estanterias}'      
        
    def __eq__(self, other):
        if (isinstance(other, Deposito)):
            return other.__numero == self.__numero
        return NotImplemented