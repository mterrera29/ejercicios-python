from empleado import Empleado

# Ejercicio 4
class Empresa():

    def __init__(self, razonSocial):
        self.__razonSocial = razonSocial
        self.__productos = []
        self.__empleados = []
        
    def establecerRazonSocial(self, razonSocial):
        self.__razonSocial = razonSocial
        
    def agregarProducto(self, producto):
        self.__productos.append(producto)
        
    def removerProducto(self, producto):
        if producto in self.__productos:
            self.__productos.remove(producto)
    
    # Ejercicio 5    
    def altaEmpleado(self, empleado):
        max_legajo = 0
        for emp in self.__empleados:
            legajo_actual = emp.obtenerNumeroLegajo()
            if legajo_actual is not None and legajo_actual > max_legajo:
                max_legajo = legajo_actual
        
        nuevo_legajo = max_legajo + 1
        empleado.establecerNumeroLegajo(nuevo_legajo)
        self.__empleados.append(empleado)
        
    # Ejercicio 6
    def bajaEmpleado(self, empleado):
        if empleado in self.__empleados:
            empleado.establecerEstado(Empleado.ESTADO_BAJA) 

    def obtenerRazonSocial(self):
        return self.__razonSocial
    
    def obtenerProductos(self):
        return self.__productos
    
    #Ejercicio 7
    def obtenerEmpleadosDeAlta(self):
        empleados_alta = []
        for emp in self.__empleados:
            if emp.obtenerEstado() == Empleado.ESTADO_ALTA:
                empleados_alta.append(emp)
        return empleados_alta
        
    def obtenerEmpleadoHistorico(self):
        return self.__empleados
    
    #Ejercicio 8
    def __str__(self):
        productos_str = ', '.join(str(producto) for producto in self.__productos)
        
        empleados_alta = self.obtenerEmpleadosDeAlta()
        empleados_alta_str = ', '.join(str(empleado) for empleado in empleados_alta)
        
        return f"La razón social de la empresa es: {self.__razonSocial}.\nLos productos que vende son: {productos_str}.\nLos empleados en estado de alta son: {empleados_alta_str}\n"
    
    def __eq__(self, other):
        if isinstance(other, Empresa):
            return self.__razonSocial == other.__razonSocial
        return NotImplemented 