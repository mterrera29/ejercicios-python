from robot import Robot
from sectoresFabrica import SectoresFabrica

class TestPlanta():
    def main(self):
      fabrica = SectoresFabrica(2)
      fabrica.asignar(Robot('Robot 1'), 0)
      fabrica.asignar(Robot('Robot 1'), 1)
      print(fabrica.robotSector(0) == fabrica.robotSector(1))

if __name__ == '__main__':
    test = TestPlanta()
    test.main()