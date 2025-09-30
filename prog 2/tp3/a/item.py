class Item():
  # Atributos de clase
  numeroSiguiente= 1
  
  # Método de inicialización
  def __init__(self, descripcion):
    
  # Atributos de instancia
    self.numero = Item.numeroSiguiente
    Item.numeroSiguiente = Item.numeroSiguiente +1
    self.descripcion= descripcion
    
  #Consultas
  def obtenerNumero(self):
    return self.numero
    
  def obtenerDescripcion(self):
    return self.descripcion
    
  def __str__(self):
    return f"N°: {self.numero}. Descripcion: {self.descripcion}"
  def __eq__(self,other):
    if(isinstance(other,Item)):
      return other.numero == self.numero
    return NotImplemented