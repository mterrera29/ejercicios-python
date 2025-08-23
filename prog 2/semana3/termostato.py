class Termostato():
  # Método de inicialización
  def __init__(self, s, p):
  # Atributos de instancia
    self.sensado=s
    self.panel=p
  # Comandos
  def establecerSensado(self, s):
    self.sensado= s
  def establecerPanel(self, p):
    self.panel=p
  # Consultas
  def obtenerSensado(self):
    return self.sensado
  def obtenerPanel(self):
    return self.panel
  def regulado(self):
    return self.sensado==self.panel