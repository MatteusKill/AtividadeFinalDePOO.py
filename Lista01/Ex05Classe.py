class Funcionario:
    def __init__(self, nome: str, sobrenome: str, horas_trabalhadas: float, valor_hora: float):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora
 
    def nome_completo(self):
        print(self.nome + " " + self.sobrenome)
 
    def calcular_salario(self):
        salario = self.horas_trabalhadas * self.valor_hora
        print(f"Salário do mês: R$ {salario:.2f}")
 
    def incrementar_horas(self, horas_adicionais: float):
        self.horas_trabalhadas += horas_adicionais
 