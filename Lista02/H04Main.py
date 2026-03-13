cores = {"limpa": "\033[m", "amarelo": "\033[33m"}

from H04Classe import PassagemBus, PassagemAviao

bus01 = PassagemBus(120.00, "15A", "ABC-1234", leito=True)
bus01.escolher_assento("20B")
bus01.abastecer()

print()

aviao01 = PassagemAviao(850.00, "32F", "G7", checkin_feito=True)
aviao01.escolher_assento("32F")
aviao01.decolar()
