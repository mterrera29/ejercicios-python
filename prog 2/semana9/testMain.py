from planta import Planta
from fecha import Fecha
from empleado import Empleado

class TestPlanta():
    def main(self):
        personal = Planta(4)
        fecha1 = Fecha(20, 4, 2010)
        fecha2 = Fecha(20, 10, 2012)
        empleados = []
        empleados.append(Empleado(123, 20000, fecha1))
        empleados.append(Empleado(124, 30000, fecha2))
        empleados.append(Empleado(154, 25000, fecha1))
        empleados.append(Empleado(150, 22000, fecha1))
        for i in range(len(empleados)):
          personal.alta(empleados[0])
        print(personal.basicoRango(25000, 30000))

if __name__ == '__main__':
    test = TestPlanta()
    test.main()