cores = {
    "limpa": "\033[m",
    "amarelo": "\033[33m",
    "vermelho": "\033[31m"
}

from Ex07Classe import Agenda

dia = int(input("Informe o dia: "))
mes = int(input("Informe o mês: "))
ano = int(input("Informe o ano: "))
anotacao = input("Informe a anotação: ")

agenda01 = Agenda(dia, mes, ano, anotacao)

if not agenda01.validar_data():
    print(f"{cores['vermelho']}Data inválida!{cores['limpa']}")
else:
    print(f"{cores['amarelo']}Anotação registrada:{cores['limpa']}")
    agenda01.mostrar_anotacao()

    nova_anotacao = input("Informe uma nova anotação para sobrescrever: ")
    agenda01.anotar_tarefa(nova_anotacao)

    print(f"{cores['amarelo']}Anotação atualizada:{cores['limpa']}")
    agenda01.mostrar_anotacao()
