class Pelota:
    def __init__(self):
        self.estado = 'FRENADA'

    def obtenerEstado(self):
        return self.estado

    def rodar(self):
        print('Rodando...')
        self.estado = 'RODANDO'

    def frenar(self):
        print('Frenando...')
        self.estado = 'FRENADA'

    def imprimirEstado(self):
        print('Estado: ' + self.estado)


class PelotaConNombre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__establecerEstadoInicial()

    def __establecerEstadoInicial(self):
        self._establecerEstado('FRENADA')

    def _establecerEstado(self, estado):
        self.estado = estado

    def establecerNombre(self, nombre):
        self.nombre = nombre

    def obtenerEstado(self):
        return self.estado

    def obtenerNombre(self):
        return self.nombre

    def rodar(self):
        print('Rodando...')
        self._establecerEstado('RODANDO')

    def frenar(self):
        print('Frenando...')
        self._establecerEstado('FRENADA')

    def imprimirEstado(self):
        print('Estado de ' + self.nombre + ': ' + self.estado)
