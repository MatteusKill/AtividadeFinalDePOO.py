from Ex04Classe import Conta

nome_usuario = input("Informe o seu nome: ")
cpf_usuario = int(input("Informe o seu cpf: "))
numero_conta_usuario = int(input("Informe o numero da sua conta: "))
saldo_conta = float(input("Informe o valor do saldo disponível na conta: "))

usuario01 = Conta(nome_usuario, cpf_usuario,numero_conta_usuario,saldo_conta)

valor_deposito_conta = float(input("Informe a quantida do valor a ser depositado: "))
usuario01.depositar(valor_deposito_conta)
print(f"Deposito realizado! Saldo atual: {usuario01.imprimir_saldo()}")

valor_saque_conta = float(input("Informe o valor do saque: "))
if not usuario01.sacar(valor_saque_conta):
    print("Erro! valor do saque maior que o valor do saldo atual.")
else:
    print(f"Saldo atual: {usuario01.imprimir_saldo()}")