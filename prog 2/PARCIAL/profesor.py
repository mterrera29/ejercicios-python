class Profesor:
  edadJubilatoria= 65
  def __init__(self, l, e, d):
    self.legajo = l
    self.edad = e
    self.dedicacion = d
  #Comandos
  def establecerLegajo(self,l):
    self.legajo = l
  def establecerEdad(self,e):
    self.legajo = e
  def establecerDedicacion(self,d):
    self.legajo = d
  def copy(self,p):
    self.legajo = p.obtenerLegajo()
    self.edad = p.obtenerEdad()
    self.dedicacion = p.obtenerDedicacion()
  #consultas
  def obtenerLegajo(self):
    return self.legajo
  def obtenerEdad(self):
    return self.edad
  def obtenerDedicación(self):
    return self.dedicacion
  def obtenerEdadJubilatoria(self):
    return self.edadJubilatoria
  def equals(self,p):
    return self.legajo == p.obtenerLegajo() and self.edad == p.obtenerEdad() and self.dedicacion == p.obtenerDedicacion()
  def clone(self):
    p = Profesor(self.legajo, self.edad, self.dedicacion)
    return p
  
    
    