class Empleado():
    def __init__(self,leg,sb,fi):
        self._legajo=leg
        self._sueldoBasico=sb
        self._fechaIngreso=fi
    
    def establecerSueldoBasico(self,sb):
        self._sueldoBasico=sb
    
    def obtenerLegajo(self):
        return self._legajo
    def obtenerSueldoBasico(self):
        return self._sueldoBasico
    def obtenerFechaIngreso(self):
        return self._fechaIngreso

    def obtenerAntiguedad(self,hoy):
        '''Requiere hoy posterior a fechaIngreso. Retorna la diferencia en años entre fechaIngreso y 
        hoy o -1 si alguna de las fechas es nula'''
        d = -1
        if self._fechaIngreso != None and hoy != None:
            d = self._fechaIngreso.difFechas(hoy)
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
            sn = 2*self._sueldoBasico
        else:
            porc = pl.obtenerPorcentaje(a)
            sn = self._sueldoBasico + (self._sueldoBasico*(porc/100))
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

class Vendedor(Empleado):
    def obtenerSueldoNeto(self):
        #El sueldo neto es el sueldo básico más un 5% de las ventas acumuladas 
        return self.obtenerSueldoBasico() + (0.05 * self._ventaAcumulada)
