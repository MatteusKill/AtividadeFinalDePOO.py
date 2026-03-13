cores = {"limpa": "\033[m", "amarelo": "\033[33m"}

from H02Classe import Aluno, Professor

aluno01 = Aluno(1001, "Matteus", 20, 8.5, 7.0, 9.0, 6.5)
aluno01.apresentar()
aluno01.calcular_media()
aluno01.estudar()

print()

prof01 = Professor(2001, "Thiago Almeida", 35, "Ciência da Computação", "POO", 20, 5800.00)
prof01.apresentar()
prof01.lecionar()
prof01.mostrar_salario()
