cores = {"limpa": "\033[m", "amarelo": "\033[33m"}

from H10Classe import (Automovel, Motocicleta, Onibus,
                        AviaoMonomotor, AviaoComercial,
                        Lancha, Navio)

print(f"{cores['amarelo']}=== TERRESTRES ==={cores['limpa']}")
carro01 = Automovel("Civic", 5, 220.0, 4, "Gasolina")
carro01.mover()
carro01.abastecer()

moto01 = Motocicleta("CB 500", 2, 180.0, 500)
moto01.mover()
moto01.empinar()

onibus01 = Onibus("Expresso Campo Grande", 50, 110.0, 44)
onibus01.mover()
onibus01.embarcar_passageiros()

print()
print(f"{cores['amarelo']}=== AÉREOS ==={cores['limpa']}")
monomotor01 = AviaoMonomotor("Cessna 172", 4, 226.0, 4000.0, "PR-XYZ")
monomotor01.mover()
monomotor01.decolar()

comercial01 = AviaoComercial("Boeing 737", 180, 842.0, 12500.0, 2, "LATAM")
comercial01.mover()
comercial01.fazer_checkin()

comercial02 = AviaoComercial("Airbus A380", 555, 903.0, 13100.0, 4, "Emirates")
comercial02.mover()
comercial02.fazer_checkin()

print()
print(f"{cores['amarelo']}=== AQUÁTICOS ==={cores['limpa']}")
lancha01 = Lancha("Focker 275", 8, 85.0, 0.8, 300)
lancha01.mover()
lancha01.acelerar()

lancha02 = Lancha("Triton 260", 6, 70.0, 0.6, 200)
lancha02.mover()
lancha02.acelerar()

navio01 = Navio("MSC Grandiosa", 6334, 22.7, 8.5, 65000)
navio01.mover()
navio01.atracar()

navio02 = Navio("Ever Given", 20000, 22.8, 15.7, 220000)
navio02.mover()
navio02.atracar()
