from robot import *

""" rob = Robot("‘Pocho’")
rob.caminar()
b = rob.tieneMasEnergia(95)
print(rob.__str__())
tob = Robot("‘Nacho’")
e = rob.mayorEnergia(tob)
s = rob.conMasEnergia(tob)
nom = rob.obtenerNombre()
print(b,e,s) """

robot1 = Robot('Manuel')
robot2 = Robot('Luchi')
robot1.dormir()
for i in range(1, 5):
  if (i % 2 == 0):
    robot1.dormir()
  else:
    robot1.despertar()
for j in range(i, 5):
  if (i % 2 == 0):
    robot2.dormir()
  else:
    robot2.despertar()
    robot2.caminar()
print(robot1.conMasEnergia(robot2))