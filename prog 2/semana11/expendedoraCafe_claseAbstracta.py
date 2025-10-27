from abc import ABC, abstractmethod

class ExpendedoraCafe(ABC):
    # atributos de clase
    # medido en gramos
    _maxCafe = 1500
    # medido en mililitros
    _maxAgua = 20000

    # método de inicialización
    @abstractmethod
    def __init__(self):
        ''' atributos de instancia
            Cada depósito se carga completo
        '''
        self._cantCafe = self._maxCafe
        self._cantAgua = self._maxAgua
    
    def cafe(self):
        # requiere disponibles 40 gramos de café y 200 ml de agua
        self._cantCafe -= 40
        self._cantAgua -= 200
    
    def recargarCafe(self):
        # carga el depósito completo
        self._cantCafe = self._maxCafe
    
    def recargarAgua(self):
        # carga el depósito completo
        self._cantAgua = self._maxAgua
    
    def vasosCafe(self):
        # computa cuántos vasos de café pueden prepararse con las cantidades disponibles
        c = int(self._cantCafe / 40)
        a = int(self._cantAgua / 200)
        if c < a:
            return c
        else:
            return a
    
    def obtenerCafe(self):
        return self._cantCafe
    
    def obtenerAgua(self):
        return self._cantAgua

    @abstractmethod
    def equals(self,e):
        return self._cantCafe == e.obtenerCafe() and self._cantAgua == e.obtenerAgua() 

class M111(ExpendedoraCafe):
    # atributo de clase
    # gramos
    _maxLeche = 600
    def __init__(self):
        super().__init__()
        self._cantLeche = self._maxLeche
    def cafeConLeche(self):
        # requiere disponibles 40 gramos de café, 200 ml de agua y 20 grs de leche
        self.cafe()
        self._cantLeche -= 20
    def recargarLeche(self):
        # carga el depósito completo
        self._cantLeche = self._maxLeche
    def vasosCafeConLeche(self):
        # computa cuántos vasos pueden prepararse
        c = self.vasosCafe()
        l = int(self._cantLeche /20)
        if c < l:
            return c
        else:
            return l

    def equals(self,e: ExpendedoraCafe):
        es = False
        if isinstance(e,M111):
            es = super().equals(e) and self._cantLeche == e.obtenerLeche()