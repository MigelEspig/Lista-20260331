class contaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
contaQualquer = contaBancaria('João', 1000.00)

def exibir_saldo():
    print(f'Titular: {contaQualquer.titular}')
    print(f'Saldo: R${contaQualquer.saldo:.2f}')


contaQualquer.depositar(50.00)
exibir_saldo()