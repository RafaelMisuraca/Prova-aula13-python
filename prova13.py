class ContaBancaria:
    def __init__(self, _titular, _saldo):
        self.titular = _titular
        self.saldo = _saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado com sucesso.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de {valor} realizado com sucesso.")

    def consultar_saldo(self):
        print(f"Saldo atual: {self.saldo}")


conta = ContaBancaria("João", 1000)
conta.depositar(500)
conta.sacar(200)
conta.consultar_saldo()