cores = {"limpa": "\033[m", "amarelo": "\033[33m"}

from H08Classe import Casa, Condominio, Apartamento, Terreno, Chacara

imoveis = [
    Casa("IM-001", 1800.00, 960.00, 3, True, 120.0),
    Condominio("IM-002", 2200.00, 600.00, True, 350.00),
    Apartamento("IM-003", 1500.00, 480.00, 2, True, 8),
    Terreno("IM-004", 500.00, 240.00, 300.0),
    Chacara("IM-005", 3500.00, 1200.00, 5000.0, True),
]

print(f"{cores['amarelo']}=== IMÓVEIS DISPONÍVEIS ==={cores['limpa']}")
for imovel in imoveis:
    imovel.descrever()
    imovel.obter_parcela_iptu()
    print()
