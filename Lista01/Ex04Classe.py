class Conta:
    def __init__(self, nome, cpf, numero, saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor_deposito):
        self.saldo = self.saldo + valor_deposito
        return self.saldo
    
    def sacar(self, valor_saque):
       if self.saldo >= valor_saque:
           self.saldo= self.saldo - valor_saque
           return True
       else:
           self.saldo = False
           return self.saldo


    def imprimir_saldo(self):
        return self.saldo