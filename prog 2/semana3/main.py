from termostato import *

termostato1=Termostato(20,22)

if termostato1.regulado():
  print("Esta regulado")
else:
  print("No esta regulado")
  
termostato1.establecerSensado(22)
print(termostato1.obtenerSensado())
print(termostato1.obtenerPanel())
if termostato1.regulado():
  print("Esta regulado")
else:
  print("No esta regulado")