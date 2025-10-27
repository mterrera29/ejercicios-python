from fecha import Fecha

class Prestamo:
  def __init__(self, l, fp, d, s):
    self.libro = l
    self.fechaPrestamo = fp
    self.dias = d
    self.socio = s
    self.fechaDevolucion = None  
    
  # Comandos
  def establecerFechaDev(self, fd):
    self.fechaDevolucion = fd
    
  # Consultas
  def obtenerLibro(self):
    return self.libro
  
  def obtenerFechaPrestamo(self):
    return self.fechaPrestamo
  
  def obtenerPlazoDev(self):
    return self.fechaPrestamo.sumaDias(self.dias)
  
  def obtenerFechaDev(self):
     return self.fechaDevolucion
  
  def obtenerSocio(self):
    return self.socio
  
  def estaAtrasado(self, hoy):
    if not isinstance(self.fechaDevolucion, Fecha):
        plazo = self.obtenerPlazoDev()
        return hoy.esPosterior(plazo)
    else:
        plazo = self.obtenerPlazoDev()
        return self.fechaDevolucion.esPosterior(plazo)
        
  def penalizacion(self):
    if not isinstance(self.fechaDevolucion, Fecha):
        return None  

    plazoDev = self.obtenerPlazoDev()
    if not self.fechaDevolucion.esPosterior(plazoDev):
        return None 
    
    atraso = 0
    fechaTemp = plazoDev
    while fechaTemp.esAnterior(self.fechaDevolucion):
        atraso += 1
        fechaTemp = fechaTemp.diaSiguiente()
    
    if atraso < 7:
        diasPenalizacion = 3
    elif atraso < 21:
        diasPenalizacion = 5
    else:
        diasPenalizacion = 10
    
    return self.fechaDevolucion.sumaDias(diasPenalizacion)
  
  def equals(self, p):
    if self.libro == p.libro:
       if self.fechaPrestamo == p.obtenerFechaPrestamo():
          return True
    return False