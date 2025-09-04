class Persona():
  def __init__(self,n, a):
    self.nombre= n
    self.apellido= a
    self.grupoSanguineo= "A"
    self.altura= 0 
    
  # Comandos
  def establecerNombres(self,n):
    self.nombre = n
  def establecerApellidos(self,a):
    self.apellido = a
  def establecerGrupoSanguineo(self,gs):
    self.grupoSanguineo = gs
  def establecerAltura(self,alt):
    self.altura = alt
      
  #consultas
  def obtenerNombres(self):
    return print(self.nombre)
  def obtenerApellidos(self):
    return print(self.apellido )
  def obtenerNombreCompleto(self):
    return print(self.nombre +" "+self.apellido)
  def obtenerGrupoSanguineo(self):
    return print(self.grupoSanguineo) 
  def obtenerAltura(self):
    return print(self.altura )