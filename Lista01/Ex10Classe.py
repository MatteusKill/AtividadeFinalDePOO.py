class Carro:
    def __init__(self, modelo: str, marca: str, cor: str, ano: int, valor: float, consumo: float, nivel: float = 0):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.consumo = consumo  # km por litro
        self.nivel = nivel      # litros no tanque (default 0)

    def abastecer(self, litros: float):
        self.nivel += litros
        print(f"Abastecido! Nível atual do tanque: {self.nivel:.2f}L")

    def andar(self, distancia_km: float):
        litros_necessarios = distancia_km / self.consumo
        if litros_necessarios > self.nivel:
            print("Combustível insuficiente para percorrer essa distância!")
        else:
            self.nivel -= litros_necessarios
            print(f"Andou {distancia_km:.1f}km. Combustível restante: {self.nivel:.2f}L")

    def verificar_nivel(self):
        print(f"Nível atual do tanque: {self.nivel:.2f}L")
        print(f"Autonomia estimada: {self.nivel * self.consumo:.1f}km")

    def calcular_imposto(self) -> float:
        ipva = self.valor * 0.025
        return ipva
