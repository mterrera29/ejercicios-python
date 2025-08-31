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
robot2.dormir()
robot1.despertar()
robot2.despertar()
for i in range(1, 10): 
    robot1.caminar()
for i in range(10, 1, -1): 
    robot2.caminar()
robot1.conMasEnergia(robot2)

print(robot1,robot2)
print(robot1==robot2)