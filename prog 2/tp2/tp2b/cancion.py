class Cancion:
  def __init__(self,n,d,g):
    self.nombre = n
    self.duracion = d
    self.genero = g
  #Consultas
  def establecerNombre(self,n):
    self.nombre = n
  def establecerDuracion(self,d):
    self.duracion = d
  def establecerGenero(self,g):
    self.genero = g
  #Consultas
  def obtenerNombre(self):
    return self.nombre
  def obtenerDuracion(self):
    return self.duracion
  def obtenerGenero(self):
    return self.genero