class Nota_Fiscal:
    def __init__(self, numero: int, tipo: str, serie: int, cnpj: str,
                 razao_social: str, data: str, valor_produtos: float,
                 icms: float, frete: float, ipi: float):
        self.numero = numero
        self.tipo = tipo               # "Entrada" ou "Saída"
        self.serie = serie             # 1, 2 ou 3
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.valor_produtos = valor_produtos
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_total = 0.0

    def obter_numero(self) -> int:
        return self.numero

    def obter_data_emissao(self) -> str:
        return self.data

    def alterar_razao_social(self, nova_razao: str):
        self.razao_social = nova_razao

    def calcular_valor_total(self) -> float:
        self.valor_total = self.valor_produtos + self.frete + self.icms + self.ipi
        return self.valor_total
