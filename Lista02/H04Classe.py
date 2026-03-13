class Passagem:
    def __init__(self, preco: float, assento: str):
        self.preco = preco
        self.assento = assento

    def alterar_preco(self, novo_preco: float):
        self.preco = novo_preco
        print(f"Novo preço: R$ {self.preco:.2f}")

    def escolher_assento(self, novo_assento: str):
        self.assento = novo_assento
        print(f"Assento escolhido: {self.assento}")


class PassagemBus(Passagem):
    def __init__(self, preco: float, assento: str, placa: str, leito: bool):
        super().__init__(preco, assento)
        self.placa = placa
        self.leito = leito

    def abastecer(self):
        print(f"Ônibus {self.placa} abastecido e pronto para partir!")


class PassagemAviao(Passagem):
    def __init__(self, preco: float, assento: str, portao_embarque: str, checkin_feito: bool):
        super().__init__(preco, assento)
        self.portao_embarque = portao_embarque
        self.checkin_feito = checkin_feito

    def decolar(self):
        if self.checkin_feito:
            print(f"Decolando pelo portão {self.portao_embarque}! Boa viagem!")
        else:
            print("Check-in não realizado. Não é possível decolar.")
