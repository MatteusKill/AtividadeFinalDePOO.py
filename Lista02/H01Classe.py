class Filme:
    def __init__(self, nome: str, duracao: int):
        self.nome = nome
        self.duracao = duracao  # em minutos

    def play(self):
        print(f"Dando play em '{self.nome}' ({self.duracao} min)")


class Acao(Filme):
    def __init__(self, nome: str, duracao: int, num_explosoes: int):
        super().__init__(nome, duracao)
        self.num_explosoes = num_explosoes

    def explodir(self):
        print(f"BOOM!")


class Drama(Filme):
    def __init__(self, nome: str, duracao: int, tema: str):
        super().__init__(nome, duracao)
        self.tema = tema

    def chorar(self):
        print(f"'{self.nome}' é um drama sobre {self.tema}. Prepare os lenços.")


class Suspense(Filme):
    def __init__(self, nome: str, duracao: int, nivel_tensao: int):
        super().__init__(nome, duracao)
        self.nivel_tensao = nivel_tensao  # 1 a 10

    def revelar_vilao(self):
        print(f"SPOILER! O vilão de '{self.nome}' foi revelado! (Tensão: {self.nivel_tensao}/10)")
