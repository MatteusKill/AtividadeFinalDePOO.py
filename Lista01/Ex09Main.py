cores = {
    "limpa": "\033[m",
    "amarelo": "\033[33m"
}

from Ex09Classe import Aluno_Academia

nome = input("Informe o nome do aluno: ")
idade = int(input("Informe a idade: "))
peso = float(input("Informe o peso (kg): "))
altura = float(input("Informe a altura (m): "))

aluno01 = Aluno_Academia(nome, idade, peso, altura)

imc = aluno01.calcular_imc()
print(f"{cores['amarelo']}IMC:{cores['limpa']} {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")

mensalidade = aluno01.obter_valor_mensalidade()
print(f"{cores['amarelo']}Valor da mensalidade:{cores['limpa']} R$ {mensalidade:.2f}")

if idade < 18:
    print("(desconto de 50% aplicado por ser menor de idade)")
