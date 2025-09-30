from item  import *

class Caja():
  # Atributos de clase
  numeroSiguiente= 0
  
  # Método de inicialización
  def __init__(self, alto, ancho, profundidad, material):
    
  # Atributos de instancia
    self.alto = alto
    self.ancho= ancho
    self.profundidad= profundidad
    self.items = []
    self.material = material
  #Comandos
  def establecerAlto(self, alto):
    self.alto = alto
  def establecerAncho(self, ancho):
    self.ancho = ancho
  def establecerProfundidad(self, profundidad):
    self.profundidad = profundidad    
  def establecerMaterial(self, material):
    self.material = material
  def agregarItem(self, item):
    self.items.append(item)
  def removerItem(self, item):
    self.items.remove(item)
  
  #Consultas
  def obtenerNumero(self):
    return self.numero
  def obtenerDimensiones(self):
    return f"Alto: {self.alto}. Profundidad: {self.profundidad}. Ancho: {self.ancho}"
  def obtenerItems(self):
    return self.items 
  def obtenerMaterial(self):
    self.material