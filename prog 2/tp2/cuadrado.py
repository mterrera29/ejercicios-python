class Cuadrado:
  instanciasCreadas = 0
  def __init__(self, l):
    self.lado = l
    Cuadrado.instanciasCreadas += 1
  #Comandos
  def establecerLado(self, l):
    self.lado = l
  def obtenerLado(self):
    return print(self.lado)
  def obtenerArea(self):
    return print(self.lado * self.lado)
  def obtenerPerimetro(self):
    return print(self.lado * 4)