class ContaCorrente:
    def __init__(self, numero, titular, saldo):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

    def numero(self):
        return self.__numero
    
    def titular(self):
        return self.__titular

    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
    def __str__(self):
        return f"Conta: {self.__numero} - {self.__titular} - Saldo: R${self.__saldo:.2f}"

conta = ContaCorrente(123456, "Ricardo", 9999.99)

conta.sacar(1111.11)
print(conta.saldo())
