cores = {
    "limpa":"\033[m",
    "vermelho":"\033[31m",
    "amarelo":"\033[33m"
}

## "Do documento chamado "EX01Class" importa a Classe 'Pessoa'
from Ex01Class import Pessoa

print("EXERCICIO 01 - PESSOA")
nome_pessoa = input("Digite o seu nome: ")
idade_pessoa = int(input("Digite a sua idade: "))
endereco_pessoa = input("Digite o seu endereço: ")

## instanciei a classe e passei as variáveis acima como parametro
pessoa01 = Pessoa(nome_pessoa, idade_pessoa, endereco_pessoa)
print(f"{cores['amarelo']}Mostrando nome:{cores['limpa']}")
print(pessoa01.mostrar_nome())
print(f"{cores['amarelo']}Mostrando idade:{cores['limpa']}")
print(pessoa01.idade)

## Variável para guardar o valor da nova idade
nova_idade= int(input("Digite a nova idade: "))

##  Chama método de alterar_idade com o valor da variável acima como parâmetro
print(f"{cores['amarelo']}Mostrando nova idade:{cores['limpa']}")
pessoa01.alterar_idade(nova_idade)
print(pessoa01.idade)

## Chama o método imprimir_endereco
print(f"{cores['amarelo']}Mostrando endereço:{cores['limpa']}")
print(pessoa01.imprimir_endereco())