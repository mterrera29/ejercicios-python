#Ejercicio 2

class Empleado():
    
    ESTADO_ALTA = 1
    ESTADO_BAJA = 2
    
    def __init__(self, nombres, apellidos):
        self.__numeroLegajo = None
        self.__nombres = nombres
        self.__apellidos = apellidos
        
        #Ejercicio 3
        self.__estado = Empleado.ESTADO_ALTA

    def establecerNumeroLegajo(self, numero):
        self.__numeroLegajo = numero
        
    def establecerNombres(self, nombres):
        self.__nombres = nombres
        
    def establecerApellidos(self, apellidos):
        self.__apellidos = apellidos
    
    def establecerEstado(self, estado):
        self.__estado = estado
    
    def obtenerNumeroLegajo(self):
        return self.__numeroLegajo
    
    def obtenerNombres(self):
        return self.__nombres
    
    def obtenerApellidos(self):
        return self.__apellidos
    
    def obtenerEstado(self):
        return self.__estado


    #Ejercicio 8
    def __str__(self):
        if self.__estado == self.ESTADO_ALTA:
            estado_texto = "ALTA"
        else:
            estado_texto = "BAJA"
        return f"{self.__nombres} {self.__apellidos}"
    
    def __eq__(self, other):
        if isinstance(other, Empleado):
            return self.__numeroLegajo == other.__numeroLegajo
        return NotImplemented