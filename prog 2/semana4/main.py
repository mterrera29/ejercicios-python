from robot import *

rob = Robot("‘Pocho’")
rob.caminar()
b = rob.tieneMasEnergia(95)
print(rob.__str__())
tob = Robot("‘Nacho’")
e = rob.mayorEnergia(tob)
s = rob.conMasEnergia(tob)
nom = rob.obtenerNombre()
print(b,e,s)