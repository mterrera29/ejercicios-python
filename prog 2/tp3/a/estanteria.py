class Estanteria():
 # Atributos de clase
  numeroSiguiente= 1
  
  # Método de inicialización
  def __init__(self):
  # Atributos de instancia
    self.cajas = []
    self.numero = Estanteria.numeroSiguiente
    Estanteria.numeroSiguiente = Estanteria.numeroSiguiente + 1
  
  #Comandos
  def agregarCaja(self, caja):
    self.cajas.append(caja)
  def removerCaja(self, caja):
    self.cajas.remove(caja)
  #Consultas
  def obtenerNumero(self):
    return self.numero
    
  def obtenerEstanterias(self):
    return self.descripcion 