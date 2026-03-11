class Aluno:
    def __init__(self, nome, ra, nota1,nota2,nota3,nota4):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def mostrar_situacao(self, situacao):
        if situacao >= 7:
            print("Aprovado!")
        elif situacao > 5 and situacao < 6.9:
            print("Exame!")
        else:
            print("Reprovado!")
