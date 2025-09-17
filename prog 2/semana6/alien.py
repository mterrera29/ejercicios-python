class Alien():
    #Atributos de classe
    maxVidas = 5
    def __init__(self,nave,vidas,ojos,manos):
         # requiere nave ligado y 0<vidas<=5 
         self.vidas=vidas
         self.ojos=ojos
         self.manos=manos
         self.nave=nave
    def equals(self,alien):
        #requiere alien ligado
        return self.vidas==alien.obtenerVidas() and self.ojos==alien.obtenerOjos() and self.manos==alien.obtenerManos() and self.nave==alien.obtenerNave()  
    '''
    def equals(self,alien):
        #requiere alien ligado
        return self.vidas==alien.obtenerVidas() and self.ojos==alien.obtenerOjos() and 
        self.manos==alien.obtenerManos() and self.nave.equals(alien.obtenerNave())  
    '''