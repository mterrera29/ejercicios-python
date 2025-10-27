class Robot():
    _energiaMin=10
    _energiaMax=100
    def __init__(self,n):
        self._nombre=n
        self._estado= True
        self._pasos=0
        self._energia=self._energiaMax
    # Comandos
    def caminar(self):
        if self._estado:
            self._pasos += 1
            self._energia=self._energia - 5
            if self._energia < self._energiaMin:
                self.recargar()
    def recargar(self):
        if self._estado:
            self._energia=self._energiaMax
    def dormir(self):
        if self._estado:
            self._estado=False
            self._energia-=1
            if self._energia < self._energiaMin:
                self.recargar()
    def despertar(self):
        if not(self._estado):
            self._estado=True
            self._energia -= 1
            if self._energia < self._energiaMin:
                self.recargar()
    #consultas
    def obtenerNombre(self):
        return self._nombre
    def obtenerEstado(self):
        return self._estado
    def obtenerPasos(self):
        return self._pasos
    def obtenerEnergia(self):
        return self._energia
    def tieneMasEnergia(self,e):
        return self._energia > e
    def __str__(self):
        s = self._nombre + ' ' + str(self._estado) + ' ' + str(self._pasos) + ' ' + str(self._energia) 
        return s
    def mayorEnergia(self,r):
        if self._energia > r.obtenerEnergia():
            n = self._energia
        else:
            n = r.obtenerEnergia()
        return n
    def conMasEnergia(self,r):
        if self._energia > r.obtenerEnergia():
            n = self
        else:
            n = r
        return n
    def cantPasos(self):
        return int(self._energia / 5)



class Coach(Robot):
    # método de inicialización
    def __init__(self,n):
        # Atributos de instancia
        super().__init__(n)
        self._asistidos= 0
    # comandos
    def asistir(self):
        #self._estado = False
        if self.obtenerEstado():
            print("Hola")
            self._asistidos += 1
            self._energia -= 8
            if self._energia < 15:
                self.recargar()
    def __str__(self):
        s = super().__str__()
        return s + ' ' + str(self._asistidos)
        
class Ecorobot(Robot):
    def __init__(self, n):
        super().__init__(n)
    def caminar(self):
        if self._estado:
            self._pasos += 1
            self._energia -= 2
            if self._energia < self._energiaMin:
                self.recargar()
    def cantPasos(self):
        return int(self._energia / 2)


r = Robot("Jim")
c = Coach("Tom")
print(r.__str__())
print(c.__str__())
