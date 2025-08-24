class NaveEspacial():
    # Atributos de clase
    maxDeposito = 1000
    parsec = 100
    # Método de inicialización
    def __init__(self, o, c):
    # Atributos de instancia
        """ 
        si comb > maxDeposito, combustible=maxDeposito. 
        Requiere que o igual a 
        'V', 'R' o 'A'
        """
        self.color=o
        if c > self.maxDeposito:
            self.combustible = self.maxDeposito
        else:
            self.combustible = c
    # Comandos
    def establecerColor(self,o):
        self.color = o
    def establecerCombustible(self,c):
        if c > self.maxDeposito:
            self.combustible = self.maxDeposito
        else:
            self.combustible = c
    def llenarDeposito(self):
        self.combustible = self.maxDeposito
    # Consultas
    def obtenerColor(self):
        return self.color
    def obtenerCombustible(self):
        return self.combustible
    def obtenerAutonomia(self):
        return self.combustible / self.parsec