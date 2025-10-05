class Cliente:

    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def imprimirSaldo(self):
        print('Saldo de ' + self.nombre + ': ' + str(self.saldo))

class Cheque:

    def __init__(self, monto, cliente):
        self.estadoCobrado = False
        self.monto = monto
        self.cliente = cliente

    def cobrar(self, clienteBeneficiario):
        if not self.estadoCobrado:
            self.estadoCobrado = True
            self.cliente.saldo -= self.monto
            clienteBeneficiario.saldo += self.monto
        else:
            print('¡Cheque ya cobrado!')