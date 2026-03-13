class Brinquedo:
    def __init__(self, nome: str, cor: str, tamanho: str, preco: float):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco

    def brincar(self):
        print(f" Estou brincando com {self.nome}!")

class BuzzLightyear(Brinquedo):
    def __init__(self, cor, tamanho, preco, autonomia_voo: int):
        super().__init__("Buzz Lightyear", cor, tamanho, preco)
        self.autonomia_voo = autonomia_voo 

    def brincar(self):
        print(f" {self.nome} está voando! Autonomia: {self.autonomia_voo}m. Ao infinito e além!")


class Woody(Brinquedo):
    def __init__(self, cor, tamanho, preco, comprimento_laco: float):
        super().__init__("Woody", cor, tamanho, preco)
        self.comprimento_laco = comprimento_laco 

    def brincar(self):
        print(f"{self.nome} está laçando! Alcance do laço: {self.comprimento_laco}m. Há um cobra em minha bota!")


class CarroDeControle(Brinquedo):
    def __init__(self, cor, tamanho, preco, velocidade_max: int):
        super().__init__("Carro de Controle Remoto", cor, tamanho, preco)
        self.velocidade_max = velocidade_max 

    def brincar(self):
        print(f" {self.nome} acelerando a {self.velocidade_max}km/h!")


class BonecaBarbara(Brinquedo):
    def __init__(self, cor, tamanho, preco, profissao: str):
        super().__init__("Barbie", cor, tamanho, preco)
        self.profissao = profissao

    def brincar(self):
        print(f" {self.nome} está trabalhando como {self.profissao}!")


class LegoBloco(Brinquedo):
    def __init__(self, cor, tamanho, preco, num_pecas: int):
        super().__init__("LEGO", cor, tamanho, preco)
        self.num_pecas = num_pecas

    def brincar(self):
        print(f" Montando {self.nome} com {self.num_pecas} peças!")


class PeaoBeyblade(Brinquedo):
    def __init__(self, cor, tamanho, preco, rotacao_rpm: int):
        super().__init__("Beyblade", cor, tamanho, preco)
        self.rotacao_rpm = rotacao_rpm

    def brincar(self):
        print(f" {self.nome} girando a {self.rotacao_rpm} RPM! LET IT RIP!")


class BonecoPokemon(Brinquedo):
    def __init__(self, cor, tamanho, preco, especie: str):
        super().__init__("Pokémon", cor, tamanho, preco)
        self.especie = especie

    def brincar(self):
        print(f" {self.especie} apareceu! {self.nome} está pronto para batalhar!")


class PistaDeCorrida(Brinquedo):
    def __init__(self, cor, tamanho, preco, num_voltas: int):
        super().__init__("Pista de Corrida", cor, tamanho, preco)
        self.num_voltas = num_voltas

    def brincar(self):
        print(f" Completando {self.num_voltas} voltas na {self.nome}!")


class EspadaDeLuz(Brinquedo):
    def __init__(self, cor, tamanho, preco, lado_da_forca: str):
        super().__init__("Espada de Luz", cor, tamanho, preco)
        self.lado_da_forca = lado_da_forca

    def brincar(self):
        print(f" {self.nome} ({self.lado_da_forca}) está ativada! Vzzzzmmm!")


class IoIo(Brinquedo):
    def __init__(self, cor, tamanho, preco, num_truques: int):
        super().__init__("Ioiô", cor, tamanho, preco)
        self.num_truques = num_truques

    def brincar(self):
        print(f" {self.nome} executando {self.num_truques} truques!")
