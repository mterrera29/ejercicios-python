from Caja import *
class Robot():
    #Atributos de clase
    energiaMaxima=5000
    energiaMinima=100
    def __init__(self,nro,caja):
	    # requiere caja ligada
        self.nroSerie = nro
        self.energia = self.energiaMaxima
        self.ruedas = caja.obtenerRuedas()
        self.opticas = caja.obtenerOpticas()
        self.chasis = caja.obtenerChasis()
        caja.vaciar()
    #Comandos
    def recargar(self):
        self.energia = self.energiaMaxima
    def armarAuto(self): 
        '''Requiere que se haya controlado si hay
        piezas disponibles'''
        self.ruedas -= 4
        self.opticas -= 6
        self.energia -= 70 
        self.chasis -= 1
        #Controla si es necesario recargar energía
        if self.energia < self.energiaMinima:
            self.recargar()
    def abrirCaja(self,caja):
        '''Aumenta sus cantidades según las de la caja
        y la vacía. 
        Requiere caja ligada'''
        ruedas += caja.obtenerRuedas()
        opticas += caja.obtenerOpticas()
        chasis += caja.obtenerChasis()
        energia -= 50
        caja.vaciar()
        #Controla si es necesario recargar energía
        if self.energia < self.energiaMinima:
            self.recargar()
    #Consultas
    def obtenerRuedas(self):
        return self.ruedas
    def obtenerOpticas(self):
        return self.opticas
    def obtenerChasis(self):
        return self.chasis
    def obtenerNroSerie(self):
        return self.nroSerie
    def obtenerEnergia(self):
        return self.energia