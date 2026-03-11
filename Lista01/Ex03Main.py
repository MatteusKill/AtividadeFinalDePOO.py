cores = {
    "limpa":"\033[m",
    "vermelho":"\033[31m",
    "amarelo":"\033[33m"
}
from Ex03Classe import Aluno

nome_aluno = input("Informe o nome do aluno: ")
ra_aluno = int(input("Informe o RA do aluno: "))
nota1 = float(input("Informe a primeira nota do aluno: "))
nota2 = float(input("Informe a segunda nota do aluno: "))
nota3 = float(input("Informe a terceira nota do aluno: "))
nota4 = float(input("Informe a quarta nota do aluno: "))

aluno01 = Aluno(nome_aluno, ra_aluno, nota1, nota2, nota3, nota4)
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"{cores['amarelo']}Media:{media:.2f}{cores['limpa']}")
aluno01.mostrar_situacao(media)