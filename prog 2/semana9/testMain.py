from planta import Planta
from fecha import Fecha
from empleado import Empleado

class TestPlanta():
    def main(self):
        personal = Planta(10)
        fecha1 = Fecha(20, 4, 2010)
        fecha2 = Fecha(20, 10, 2012)
        e1 = Empleado(123, 20000, fecha1)
        e2 = Empleado(124, 30000, fecha2)
        e3 = Empleado(154, 25000, fecha1)
        e4 = Empleado(150, 22000, fecha1)
        personal.alta(e1)
        personal.alta(e2)
        print(personal.cantEmpleados())

if __name__ == '__main__':
    test = TestPlanta()
    test.main()