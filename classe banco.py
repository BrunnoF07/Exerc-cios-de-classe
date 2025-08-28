class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor:.2f} realizado com sucesso")
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saldo de R${valor:.2f} realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def exibir_saldo(self):
        print(f"Saldo atual de {self.titular}: R${self.saldo:.2f}")

conta_brunno = ContaBancaria("Brunno", 2500)

conta_brunno.depositar(500)
conta_brunno.sacar(4500)
conta_brunno.exibir_saldo()