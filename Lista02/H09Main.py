cores = {"limpa": "\033[m", "amarelo": "\033[33m"}

from H09Classe import Avista, Parcelada

compra01 = Avista(101, "Notebook", 3000.00, 0.10)
compra01.calcular_com_desconto()

print()

compra02 = Parcelada(102, "Smartphone", 2500.00, 12)
compra02.calcular_parcelas()
