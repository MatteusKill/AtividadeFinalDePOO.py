class Agenda:
    def __init__(self, dia: int, mes: int, ano: int, anotacao: str):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao

    def validar_data(self) -> bool:
        if self.mes < 1 or self.mes > 12:
            return False
        dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # verifica ano bissexto
        if (self.ano % 4 == 0 and self.ano % 100 != 0) or (self.ano % 400 == 0):
            dias_por_mes[2] = 29
        if self.dia < 1 or self.dia > dias_por_mes[self.mes]:
            return False
        return True

    def anotar_tarefa(self, nova_anotacao: str):
        self.anotacao = nova_anotacao

    def mostrar_anotacao(self):
        print(f"Data: {self.dia:02d}/{self.mes:02d}/{self.ano}")
        print(f"Anotação: {self.anotacao}")
