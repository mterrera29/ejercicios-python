class Deposito():
 # Atributos de clase
  numeroSiguiente= 0
  
  # Método de inicialización
  def __init__(self):
  # Atributos de instancia
    self.estanterias = []
    self.numero = Deposito.numeroSiguiente
    Deposito.numeroSiguiente = Deposito.numeroSiguiente + 1
    
  #Comandos 
  def agregarCaja(self, estanterias):
    self.estanterias.append(estanterias)
  def removerCaja(self, estanterias):
    self.estanterias.remove(estanterias)
    
  #Consultas
  def obtenerNumero(self):
    return self.numero
  
  def obtenerEstanterias(self):
    return self.estanterias