class Compra:
    def __init__(self, numero: int, produto: str, valor: float):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0.0

    def calcular_valor_total(self) -> float:
        icms = self.valor * 0.17
        frete = self.valor * 0.05
        self.valor_total = self.valor + icms + frete
        print(f"Produto: {self.produto} | Valor base: R$ {self.valor:.2f}")
        print(f"  ICMS (17%): R$ {icms:.2f} | Frete (5%): R$ {frete:.2f}")
        print(f"  Valor total: R$ {self.valor_total:.2f}")
        return self.valor_total


class Avista(Compra):
    def __init__(self, numero: int, produto: str, valor: float, desconto: float):
        super().__init__(numero, produto, valor)
        self.desconto = desconto

    def calcular_com_desconto(self) -> float:
        self.calcular_valor_total()
        valor_desconto = self.valor_total * self.desconto
        preco_final = self.valor_total - valor_desconto
        print(f"  Desconto à vista ({self.desconto*100:.0f}%): -R$ {valor_desconto:.2f}")
        print(f"  Preço final à vista: R$ {preco_final:.2f}")
        return preco_final


class Parcelada(Compra):
    def __init__(self, numero: int, produto: str, valor: float, num_parcelas: int):
        super().__init__(numero, produto, valor)
        self.num_parcelas = num_parcelas

    def calcular_parcelas(self) -> float:
        self.calcular_valor_total()
        valor_parcela = self.valor_total / self.num_parcelas
        print(f" {self.num_parcelas}x de R$ {valor_parcela:.2f}")
        return valor_parcela
