class Funcionario:
    def __init__(self, nome: str, matricula: int, salario: float):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.pontos = []

    def bater_ponto(self, tipo: int):
        self.pontos.append(tipo)
        status = "Entrada" if tipo == 1 else "Saída"
        print(f"{self.nome} registrou: {status} (Total registros: {len(self.pontos)})")


class Vendedor(Funcionario):
    def __init__(self, nome: str, matricula: int, salario: float, comissao: float):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao
        self.vendas_mes = 0.0

    def bater_meta(self, valor_vendido: float, meta: float):
        self.vendas_mes += valor_vendido
        if self.vendas_mes >= meta:
            bonus = self.vendas_mes * self.comissao
            print(f"{self.nome} bateu a meta! Comissão: R$ {bonus:.2f}")
        else:
            print(f"{self.nome}: R$ {self.vendas_mes:.2f} vendidos (meta: R$ {meta:.2f})")


class Gerente(Funcionario):
    def __init__(self, nome: str, matricula: int, salario: float, senha: str):
        super().__init__(nome, matricula, salario)
        self.__senha = senha

    def autenticar(self, senha_digitada: str) -> bool:
        if senha_digitada == self.__senha:
            print(f" Gerente {self.nome} autenticado com sucesso.")
            return True
        else:
            print("Senha incorreta.")
            return False
