class Aluno_Academia:
    def __init__(self, nome: str, idade: int, peso: float, altura: float, mensalidade: float = 120.00):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade

    def calcular_imc(self) -> float:
        imc = self.peso / (self.altura ** 2)
        return imc

    def obter_valor_mensalidade(self) -> float:
        # Menores de idade recebem 50% de desconto
        if self.idade < 18:
            return self.mensalidade * 0.5
        return self.mensalidade
