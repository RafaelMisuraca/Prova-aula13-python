class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor
        print(f"Depósito de {valor} realizado com sucesso.")

    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo insuficiente.")
        else:
            self._saldo -= valor
            print(f"Saque de {valor} realizado com sucesso.")

    def consultar_saldo(self):
        print(f"Saldo atual: {self._saldo}")


conta = ContaBancaria("João", 1000)
conta.depositar(500)
conta.sacar(200)
conta.consultar_saldo()
