cores = {
    "limpa": "\033[m",
    "amarelo": "\033[33m"
}

from Ex06Classe import Circulo

raio = float(input("Informe o raio do círculo: "))

circulo01 = Circulo(raio)

print(f"{cores['amarelo']}Raio:{cores['limpa']}")
circulo01.imprimir_raio()

print(f"{cores['amarelo']}Área:{cores['limpa']}")
print(f"{circulo01.calcular_area():.4f}")

print(f"{cores['amarelo']}Circunferência:{cores['limpa']}")
print(f"{circulo01.calcular_circunferencia():.4f}")
