class Planta():
    # método de inicialización
    def __init__(self,max):
        # crea una colección con max elementos
        self.__listEmp=[None]*max
        self.__cant=0
    
    def alta(self, emp):
        '''Asigna el empleado emp a la primera posición 
        libre de la estructura. Aumenta el valor de cant. 
        Requiere que la clase cliente haya verificado que la estructura 
        no esté llena, emp esté ligado y no haya un empleado con el mismo número de legajo'''
        self.__listEmp[self.__cant] = emp
        self.__cant +=1

    def aumentarBasico(self,p):
        for i in range(self.cantEmpleados()):
            aumento = self.__listEmp[i].obtenerSueldoBasico() + (self.__listEmp[i].obtenerSueldoBasico()*(p / 100))
            self.__listEmp[i].establecerSueldoBasico(aumento)

    def cantEmpleados(self):
        return self.__cant

    def estaLlena(self):
        return self.__cant == len(self.__listEmp) 

    def estaEmpleado(self,leg):
        # Retorna true si la planta tiene un empleado con ese legajo    
        esta = False	    
        i = 0
        while not esta and i < self.cantEmpleados():
            if self.__listEmp[i].obtenerLegajo() == leg:
                esta = True
            else:
                i += 1
        return esta
    
    def basicoRango(self,limI,limS):
        '''Computa la cantidad de empleados que tienen sueldo básico dentro
        del rango limI,limS inclusive. Requiere que limI menor o igual a
        limS.'''
        cont = 0	    
        for i in range(self.cantEmpleados()):
            if self.__listEmp[i].obtenerSueldoBasico() >= limI and self.__listEmp[i].obtenerSueldoBasico() <= limS:
                cont += 1
        return cont 
    
    def netoRango(self,limI,limS,plant,hoy):
        '''Computa la cantidad de empleados que tienen sueldo
        neto dentro del rango limI,limS inclusive.'''
        cont = 0	    
        for i in range(self.cantEmpleados()):
            if self.__listEmp[i].obtenerSueldoNeto(plant,hoy) >= limI and self.__listEmp[i].obtenerSueldoNeto(plant,hoy) <= limS:
                cont += 1
        return cont
    
    def masVacaciones(self,v,hoy):
        '''Genera una colección con los empleados con más de v
        días de vacaciones.'''
        nuevaPlanta = Planta(self.cantEmpleados())
        for i in range(self.cantEmpleados()):
            if self.__listEmp[i].obtenerVacaciones(hoy) > v:
                nuevaPlanta.alta(self.__listEmp[i])
        return nuevaPlanta

    def baja(self,leg):
        '''Busca un empleado con legajo leg en la colección, si
        lo encuentra arrastra los empleados que siguen una posición'''    
        esta = False	    
        i = 0
        while not esta and i < self.cantEmpleados():
            if self.__listEmp[i].obtenerLegajo() == leg:
                esta = True
            else:
                i += 1
        if esta:
            self.__cant -= 1
            self.__arrastrar(i)
    
    def __arrastrar(self,i):
        '''Arrastra todos los elementos una posición
        hacia arriba'''     
        while i < self.cantEmpleados():
            self.__listEmp[i] = self.__listEmp[i+1]
            i += 1
        self.__listEmp[i] = None    