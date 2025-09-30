class Item():
  # Atributos de clase
  numeroSiguiente= 0
  
  # Método de inicialización
  def __init__(self, numero, descripcion):
    
  # Atributos de instancia
    self.numero = numero
    self.descripcion= descripcion
    
  #Consultas
  def obtenerNumero(self):
    return self.numero
    
  def obtenerDescripcion(self):
    return self.descripcion
    
  