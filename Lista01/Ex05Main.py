cores = {
    "limpa": "\033[m",
    "amarelo": "\033[33m"
}

from Ex05Classe import Funcionario

nome = input("Informe o nome do funcionário: ")
sobrenome = input("Informe o sobrenome: ")
horas = float(input("Informe as horas trabalhadas no mês: "))
valor_hora = float(input("Informe o valor por hora: "))

funcionario01 = Funcionario(nome, sobrenome, horas, valor_hora)

print(f"{cores['amarelo']}Nome completo:{cores['limpa']}")
funcionario01.nome_completo()

print(f"{cores['amarelo']}Calculando salário:{cores['limpa']}")
funcionario01.calcular_salario()

horas_extras = float(input("Informe as horas extras a incrementar: "))
funcionario01.incrementar_horas(horas_extras)

print(f"{cores['amarelo']}Salário após horas extras:{cores['limpa']}")
funcionario01.calcular_salario()