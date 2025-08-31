class Robot():
    energiaMin=10
    energiaMax=100
    def __init__(self,n):
        self.nombre=n
        self.estado= True
        self.pasos=0
        self.energia=self.energiaMax
    # Comandos
    def caminar(self):
        if self.estado:
            self.pasos += 1
            self.energia=self.energia - 5
            if self.energia < self.energiaMin:
                self.recargar()
    def dormir(self):
        if self.estado:
            self.estado=False
            self.energia-=1
            if self.energia < self.energiaMin:
                self.recargar()
    def despertar(self):
        if not(self.estado):
            self.estado=True
            self.energia -= 1
            if self.energia < self.energiaMin:
                self.recargar()
    def recargar(self):
        if self.estado:
            self.energia=self.energiaMax
    #consultas
    def obtenerNombre(self):
        return self.nombre
    def obtenerEstado(self):
        return self.estado
    def obtenerPasos(self):
        return self.pasos
    def obtenerEnergia(self):
        return self.energia
    def tieneMasEnergia(self,e):
        return self.energia > e
    def __str__(self):
        s = self.nombre + ' ' + str(self.estado) + ' ' + str(self.pasos) + ' ' + str(self.energia) 
        return s
    def mayorEnergia(self,r):
        if self.energia > r.obtenerEnergia():
            n = self.energia
        else:
            n = r.obtenerEnergia()
        return n
    def conMasEnergia(self,r):
        if self.energia > r.obtenerEnergia():
            n = self
        else:
            n = r
        return n