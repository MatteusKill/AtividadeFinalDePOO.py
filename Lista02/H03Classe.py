class Ingresso:
    def __init__(self, preco: float, setor: str):
        self.preco = preco
        self.setor = setor

    def alterar_preco(self, novo_preco: float):
        self.preco = novo_preco
        print(f"Preço atualizado para R$ {self.preco:.2f}")

    def mostrar_setor(self):
        print(f"Setor: {self.setor}, Preço: R$ {self.preco:.2f}")


class IngressoVIP(Ingresso):
    def __init__(self, preco: float, setor: str,
                 camarote: bool, open_bar: bool, open_food: bool, estacionamento: bool):
        super().__init__(preco, setor)
        self.camarote = camarote
        self.open_bar = open_bar
        self.open_food = open_food
        self.estacionamento = estacionamento

    def pegar_bebida(self):
        if self.open_bar:
            print("🍹 Open bar liberado! Aproveite!")
        else:
            print("Este ingresso não inclui open bar.")

    def acessar_camarote(self):
        if self.camarote:
            print("🎭 Acesso ao camarote liberado!")
        else:
            print("Este ingresso não inclui acesso ao camarote.")
