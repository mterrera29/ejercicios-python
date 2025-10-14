from robot import Robot
from sectoresFabrica import SectoresFabrica

class TestPlanta():
    def main(self):
      fabrica = SectoresFabrica(2)
      r1 = Robot('Robot 1')
      r2 = Robot('Robot 2')
      print(fabrica.existeSector(2))

if __name__ == '__main__':
    test = TestPlanta()
    test.main()