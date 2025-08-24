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
