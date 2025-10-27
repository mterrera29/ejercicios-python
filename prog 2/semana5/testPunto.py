from punto import *
# Creación de los puntos
p1 = Punto(2.0, 5.0)
p2 = Punto(5.0, 5.0)
p3 = Punto(2.0, 5.0)
p4 = p2.clone()
p5 = p4

# Evaluación de las expresiones
print("1. p1==p2:", p1 == p2)
print("2. p1.equals(p2):", p1.equals(p2))
print("3. p2==p3:", p2 == p3)
print("4. p3.equals(p1):", p3.equals(p1))
print("5. p2.equals(p1):", p2.equals(p1))
print("6. p1.equals(p4):", p1.equals(p4))
print("7. p4==p2:", p4 == p2)
print("8. p5==p4:", p5 == p4)
print("9. p3.equals(p5):", p3.equals(p5))
print("10. p4.equals(p3):", p4.equals(p3))