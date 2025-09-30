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
  
  def __str__(self):
    estanterias = ",".join(str(estanteria) for estanteria in self.cajas)
    return f"N°: {self.numero}. Estanterias: {estanterias}"
  def __eq__(self,other):
    if(isinstance(other,Deposito)):
      return other.numero == self.numero
    return NotImplemented