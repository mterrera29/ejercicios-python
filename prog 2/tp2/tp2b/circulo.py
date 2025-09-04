import math
class Circulo():
  PI = math.pi
  def __init__(self,r):
    self.radio= r
  #Comandos
  def establecerRadio(self,r):
    self.radio=r
  
  #consultas
  def obtenerRadio(self):
    return self.radio
  def obtenerDiametro(self):
    return 2 * self.radio
  def obtenerPerimetro(self):
    return 2 * self.PI * self.radio
  def obtenerArea(self):
    return self.PI * self.radio**2