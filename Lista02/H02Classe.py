class Pessoa:
    def __init__(self, matricula: int, nome: str, idade: int):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Nome: {self.nome}, Matrícula: {self.matricula}, Idade: {self.idade}")


class Aluno(Pessoa):
    def __init__(self, matricula: int, nome: str, idade: int,
                 nota1: float, nota2: float, nota3: float, nota4: float):
        super().__init__(matricula, nome, idade)
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.media = 0.0

    def calcular_media(self):
        self.media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
        print(f"Média de {self.nome}: {self.media:.2f}")
        return self.media

    def estudar(self):
        print(f"{self.nome} está estudando...")


class Professor(Pessoa):
    def __init__(self, matricula: int, nome: str, idade: int,
                 formacao: str, disciplina: str, carga_horaria: int, salario: float):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga_horaria = carga_horaria
        self.salario = salario

    def lecionar(self):
        print(f"Prof. {self.nome} está ensinando {self.disciplina} ({self.carga_horaria}h/semana)")

    def mostrar_salario(self):
        print(f"Salário de {self.nome}: R$ {self.salario:.2f}")
