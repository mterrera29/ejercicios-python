class Empleado():
    def __init__(self,leg,sb,fi):
        self.__legajo=leg
        self.__sueldoBasico=sb
        self.__fechaIngreso=fi
    
    def establecerSueldoBasico(self,sb):
        self.__sueldoBasico=sb
    
    def obtenerLegajo(self):
        return self.__legajo
    def obtenerSueldoBasico(self):
        return self.__sueldoBasico
    def obtenerFechaIngreso(self):
        return self.__fechaIngreso

    def obtenerAntiguedad(self,hoy):
        '''Requiere hoy posterior a fechaIngreso. Retorna la diferencia en años entre fechaIngreso y 
        hoy o -1 si alguna de las fechas es nula'''
        d = -1
        if self.__fechaIngreso != None and hoy != None:
            d = self.__fechaIngreso.difFechas(hoy)
        return d
    
    def obtenerSueldoNeto(self,pl,hoy):
        '''Requiere pl ligada y hoy posterior a fechaIngreso.
           Retorna el sueldo neto del empleado calculado como el sueldo basico incrementado según un 
           porcentaje dependiente de la antiguedad y obtenido de la planilla pl.
           Si tiene 15 años o más el sueldo neto es el doble del básico. 
        '''
        a = self.obtenerAntiguedad(hoy)
        sn = 0
        if a >= 15:
            sn = 2*self.__sueldoBasico
        else:
            porc = pl.obtenerPorcentaje(a)
            sn = self.__sueldoBasico + (self.__sueldoBasico*(porc/100))
        return sn
    
    def obtenerVacaciones(self, hoy):
        '''
        Requiere hoy posterior a fechaIngreso. Retorna la cantidad de dias de vacaciones que le 
        corresponde al empleado.
        7 si antiguedad es mayor o igual a 1 y menor o igual a 5
        15 si antiguedad es mayor a 5 y menor o igual a 10
        25 si antiguedad es mayor a 10
        Si tiene menos de 1 año no tiene vaciones.
        '''
        a = self.obtenerAntiguedad(hoy)
        v = 0
        if a > 10:
            v = 25
        else:
            if a > 5:
                v = 15
            else:
                if a >= 1:
                    v = 7
        return v   