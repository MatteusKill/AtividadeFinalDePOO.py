import math

class Circulo:
    def __init__(self, raio: float):
        self.raio = raio

    def imprimir_raio(self):
        print(f"Raio: {self.raio}")

    def calcular_area(self):
        area = math.pi * self.raio ** 2
        return area

    def calcular_circunferencia(self):
        circunferencia = 2 * math.pi * self.raio
        return circunferencia
