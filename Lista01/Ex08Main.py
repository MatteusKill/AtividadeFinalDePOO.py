cores = {
    "limpa": "\033[m",
    "amarelo": "\033[33m"
}

from Ex08Classe import Triangulo

lado_a = float(input("Informe o lado A do triângulo: "))
lado_b = float(input("Informe o lado B do triângulo: "))
lado_c = float(input("Informe o lado C do triângulo: "))

triangulo01 = Triangulo(lado_a, lado_b, lado_c)

print(f"{cores['amarelo']}Perímetro:{cores['limpa']}")
print(f"{triangulo01.calcular_perimetro():.2f}")

print(f"{cores['amarelo']}Maior lado:{cores['limpa']}")
print(f"{triangulo01.get_maior_lado():.2f}")
