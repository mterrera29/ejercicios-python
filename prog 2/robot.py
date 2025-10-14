class Robot():
    __energiaMin=10
    __energiaMax=100
    def __init__(self,n):
        self.__nombre=n
        self.__estado= True
        self.__pasos=0
        self.__energia=self.__energiaMax
    # Comandos
    def caminar(self):
        if self.__estado:
            self.pasos += 1
            self.__energia=self.__energia - 5
            if self.__energia < self.__energiaMin:
                self.recargar()
    def dormir(self):
        if self.__estado:
            self.__estado=False
            self.__energia-=1
            if self.__energia < self.__energiaMin:
                self.recargar()
    def despertar(self):
        if not(self.__estado):
            self.__estado=True
            self.__energia -= 1
            if self.__energia < self.__energiaMin:
                self.recargar()
    def recargar(self):
        if self.__estado:
            self.__energia=self.__energiaMax
    #consultas
    def obtenerNombre(self):
        return self.__nombre
    def obtenerEstado(self):
        return self.__estado
    def obtenerPasos(self):
        return self.__pasos
    def obtenerEnergia(self):
        return self.__energia
    def tieneMasEnergia(self,e):
        return self.__energia > e
    def __str__(self):
        s = self.__nombre + ' ' + str(self.__estado) + ' ' + str(self.__pasos) + ' ' + str(self.__energia) 
        return s
    def mayorEnergia(self,r):
        if self.__energia > r.obtenerEnergia():
            n = self.__energia
        else:
            n = r.obtenerEnergia()
        return n
    def conMasEnergia(self,r):
        if self.__energia > r.obtenerEnergia():
            n = self
        else:
            n = r
        return n
    def cantPasos(self):
        pass

