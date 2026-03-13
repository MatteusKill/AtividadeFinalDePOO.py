cores = {"limpa": "\033[m", "amarelo": "\033[33m"}

from H07Classe import (BuzzLightyear, Woody, CarroDeControle, BonecaBarbara,
                        LegoBloco, PeaoBeyblade, BonecoPokemon,
                        PistaDeCorrida, EspadaDeLuz, IoIo)

brinquedos = [
    BuzzLightyear("branco", "médio", 89.90, 50),
    Woody("marrom", "médio", 79.90, 2.5),
    CarroDeControle("vermelho", "pequeno", 149.90, 25),
    BonecaBarbara("rosa", "pequeno", 59.90, "astronauta"),
    LegoBloco("colorido", "grande", 299.90, 500),
    PeaoBeyblade("azul", "pequeno", 49.90, 3000),
    BonecoPokemon("amarelo", "pequeno", 39.90, "Pikachu"),
    PistaDeCorrida("cinza", "grande", 199.90, 10),
    EspadaDeLuz("azul", "médio", 119.90, "lado da luz"),
    IoIo("verde", "pequeno", 19.90, 5),
]

for brinquedo in brinquedos:
    brinquedo.brincar()
