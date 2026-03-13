class Imovel:
    def __init__(self, inscricao_municipal: str, valor_aluguel: float, iptu_anual: float):
        self.inscricao_municipal = inscricao_municipal
        self.valor_aluguel = valor_aluguel
        self.iptu_anual = iptu_anual

    def obter_parcela_iptu(self, num_parcelas: int = 12) -> float:
        parcela = self.iptu_anual / num_parcelas
        print(f"Parcela do IPTU ({num_parcelas}x): R$ {parcela:.2f}")
        return parcela

    def set_valor_aluguel(self, novo_valor: float):
        self.valor_aluguel = novo_valor
        print(f"Aluguel atualizado para R$ {self.valor_aluguel:.2f}")


class Casa(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu_anual,
                 quartos: int, churrasqueira: bool, area_m2: float):
        super().__init__(inscricao_municipal, valor_aluguel, iptu_anual)
        self.quartos = quartos
        self.churrasqueira = churrasqueira
        self.area_m2 = area_m2

    def descrever(self):
        churrasco = "com churrasqueira" if self.churrasqueira else "sem churrasqueira"
        print(f"Casa | {self.quartos} quartos | {self.area_m2}m² | {churrasco} | Aluguel: R$ {self.valor_aluguel:.2f}")


class Condominio(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu_anual,
                 area_de_lazer: bool, taxa_condominio: float):
        super().__init__(inscricao_municipal, valor_aluguel, iptu_anual)
        self.area_de_lazer = area_de_lazer
        self.taxa_condominio = taxa_condominio

    def descrever(self):
        lazer = "com área de lazer" if self.area_de_lazer else "sem área de lazer"
        print(f"Condomínio | {lazer} | Taxa cond.: R$ {self.taxa_condominio:.2f} | Aluguel: R$ {self.valor_aluguel:.2f}")


class Apartamento(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu_anual,
                 quartos: int, elevador: bool, andar: int):
        super().__init__(inscricao_municipal, valor_aluguel, iptu_anual)
        self.quartos = quartos
        self.elevador = elevador
        self.andar = andar

    def descrever(self):
        elev = "com elevador" if self.elevador else "sem elevador"
        print(f" Apartamento | {self.quartos} quartos | {self.andar}° andar | {elev} | Aluguel: R$ {self.valor_aluguel:.2f}")


class Terreno(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu_anual, area_m2: float):
        super().__init__(inscricao_municipal, valor_aluguel, iptu_anual)
        self.area_m2 = area_m2

    def descrever(self):
        print(f" Terreno | {self.area_m2}m² | Aluguel: R$ {self.valor_aluguel:.2f}")


class Chacara(Imovel):
    def __init__(self, inscricao_municipal, valor_aluguel, iptu_anual,
                 area_m2: float, piscina: bool):
        super().__init__(inscricao_municipal, valor_aluguel, iptu_anual)
        self.area_m2 = area_m2
        self.piscina = piscina

    def descrever(self):
        piscina = "com piscina" if self.piscina else "sem piscina"
        print(f"Chácara | {self.area_m2}m² | {piscina} | Aluguel: R$ {self.valor_aluguel:.2f}")
