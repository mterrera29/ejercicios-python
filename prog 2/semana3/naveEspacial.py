class NaveEspacial():
    # Atributos de clase
    maxDeposito = 1000
    parsec = 100
    # Método de inicialización
    def __init__(self, co, comb):
        self.estado_alertas = False
    # Atributos de instancia
        """ 
        si comb > maxDeposito, combustible=maxDeposito. 
        Requiere que o igual a 
        'V', 'R' o 'A'
        """
        self.color=co
        if comb > self.maxDeposito:
            self.combustible = self.maxDeposito
        else:
            self.combustible = comb
    # Comandos
    def establecerEstadoAlertas(self, habilitar):
        self.estado_alertas= habilitar 
        
    def establecerColor(self,co):
        self.color = co
        
    def agregarCombustible(self,comb):
        if self.combustible + comb > self.maxDeposito:
            if self.estado_alertas:
              print("de los " +str(comb)+" litros solo se pudieron cargar "+str(self.maxDeposito- self.combustible)+" litros")              
            self.combustible = self.maxDeposito
        else:
            if self.estado_alertas:
                print("se cargaron "+str(comb) + " litros")
            self.combustible += comb
    def llenarDeposito(self):
        self.combustible = self.maxDeposito
    # Consultas
    def obtenerColor(self):
        return self.color
    def obtenerCombustible(self):
        return self.combustible
    def obtenerAutonomia(self):
        return self.combustible / self.parsec