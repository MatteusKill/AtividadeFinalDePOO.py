class Triangulo:
    def __init__(self, lado_a: float, lado_b: float, lado_c: float):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self) -> float:
        return self.lado_a + self.lado_b + self.lado_c

    def get_maior_lado(self) -> float:
        return max(self.lado_a, self.lado_b, self.lado_c)
