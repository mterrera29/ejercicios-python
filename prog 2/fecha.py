class Fecha():
    def __init__(self,d,m,a):
        self.__dia=d
        self.__mes=m
        self.__anio=a

    def establecerDia(self,d):
        self.__dia=d
    def establecerMes(self,m):
        self.__mes=m
    def establecerAnio(self,a):
        self.__anio=a
    def obtenerDia(self):
        return self.__dia
    def obtenerMes(self):
        return self.__mes
    def obtenerAnio(self):
        return self.__anio
    def esAnterior(self,f):
        esAnterior=False
        if f.obtenerAnio() == self.__anio:
            if f.obtenerMes == self.__mes:
                esAnterior = self.__dia < f.obtenerDia()
            else:
                esAnterior = self.__mes < f.obtenerMes()
        else:
            esAnterior = self.__anio < f.obtenerAnio()
        return esAnterior
    def esIgual(self,f):
        return self.__dia == f.obtenerDia() and self.__mes == f.obtenerMes() and self.__anio == f.obtenerAnio()
    def __diasDelMes(self):
        dias = 31
        if self.__mes == 2:
            if self.__bisiesto():
                dias = 29
            else: 
                dias = 28
        else:
            if self.__mes == 4 or self.__mes == 6 or self.__mes == 9 or self.__mes == 11:
                dias = 30
        return dias
    def __bisiesto(self):
        '''
        Debe ser divisible por 4
        No debe ser divisible por 100 o
        Debe ser divisible por 400
        '''
        return (self.__anio % 4 == 0) and ((self.__anio % 100 != 0) or (self.__anio % 400 == 0))
    def sumaDias(self,d):
        diaNuevaFecha = ((d % self.__diasDelMes()) + self.__dia)
        mesNuevaFecha = (self.__mes + d / self.__diasDelMes())
        anioNuevaFecha = self.__anio
        if diaNuevaFecha > self.__diasDelMes():
            diaNuevaFecha = diaNuevaFecha % self.__diasDelMes()
            mesNuevaFecha += 1
        if mesNuevaFecha > 12:
            mesNuevaFecha = mesNuevaFecha % 12
            anioNuevaFecha += 1
        return Fecha(diaNuevaFecha,mesNuevaFecha,anioNuevaFecha)
    def diaSiguiente(self):
        return self.sumaDias(1)
    def difFechas(self,hoy):
        pass 