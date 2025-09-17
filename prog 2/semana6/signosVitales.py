class SignosVitales():
    #Atributos de classe
    umbralTemp=37.5
    def __init__(self, temp, presion):
        #Atributos de instancia
        self.temperatura = temp
        self.presion = presion
    #Consultas
    def obtenerTemperatura(self):
        return self.temperatura
    def obtenerPresion(self):
        return self.presion 
    def alarma(self):
        '''Retorna true si
        temperatura > umbralTemp o hay
        Alarma de Hipertension'''
        return self.temperatura > self.umbralTemp or self.presion.alarmaHipertension()
    def __str__(self):
        return str(self.temperatura)+' '+self.presión.__str__()
    def equals(self,sigVital):
        # requiere presion ligado
        return self.temperatura == sigVital.obtenerTemperatura() and self.presion.equals(sigVital.obtenerPresion())