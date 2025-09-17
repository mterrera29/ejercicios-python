class PresionArterial():
    # Atributos de clase
    umbralMin=75
    umbralMax=40
    # Método de inicialización
    def __init__(self, min, max):
        # Requiere max > min > 0
        self.min=min
        self.max=max
    # Consultas
    def obtenerMin(self):
        return self.min
    def obtenerMax(self):
        return self.max
    def obtenerPulso(self):
        return self.max - self.min   
    def alarmaHipertension(self):
        '''
        retorna true si
        max > umbralMax o
        min > umbralMin
        '''
        return self.max > self.umbralMax or self.min > self.umbralMin
    def equals(self,preArt):
        # requiere preArt ligado
        return self.min == preArt.obtenerMin() and self.max == preArt.obtenerMax() 
    def __str__(self):
        return str(self.min)+' '+str(self.max)         
