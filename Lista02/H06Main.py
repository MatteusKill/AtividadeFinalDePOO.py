cores = {"limpa": "\033[m", "amarelo": "\033[33m"}

from H06Classe import Vendedor, Gerente

vendedor01 = Vendedor("Ana Paula", 3001, 2000.00, 0.05)
vendedor01.bater_ponto(1)
vendedor01.bater_meta(8000.00, 10000.00)
vendedor01.bater_meta(3000.00, 10000.00)

print()

gerente01 = Gerente("Roberto Farias", 1001, 8500.00, "seg@123")
gerente01.bater_ponto(1)
gerente01.autenticar("errada")
gerente01.autenticar("seg@123")
