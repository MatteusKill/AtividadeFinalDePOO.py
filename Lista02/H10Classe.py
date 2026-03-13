class Transporte:
    def __init__(self, nome: str, capacidade: int, velocidade_max: float):
        self.nome = nome
        self.capacidade = capacidade
        self.velocidade_max = velocidade_max

    def mover(self):
        print(f" {self.nome} está se movendo.")


class Terrestre(Transporte):
    def __init__(self, nome, capacidade, velocidade_max, num_rodas: int):
        super().__init__(nome, capacidade, velocidade_max)
        self.num_rodas = num_rodas

    def mover(self):
        print(f"{self.nome} rodando na estrada com {self.num_rodas} rodas.")


class Aereo(Transporte):
    def __init__(self, nome, capacidade, velocidade_max, altitude_max: float):
        super().__init__(nome, capacidade, velocidade_max)
        self.altitude_max = altitude_max 

    def mover(self):
        print(f"{self.nome} voando a até {self.altitude_max}m de altitude.")


class Aquatico(Transporte):
    def __init__(self, nome, capacidade, velocidade_max, profundidade_max: float):
        super().__init__(nome, capacidade, velocidade_max)
        self.profundidade_max = profundidade_max

    def mover(self):
        print(f"{self.nome} navegando. Profundidade máx: {self.profundidade_max}m.")

class Automovel(Terrestre):
    def __init__(self, nome, capacidade, velocidade_max, num_rodas, combustivel: str):
        super().__init__(nome, capacidade, velocidade_max, num_rodas)
        self.combustivel = combustivel

    def abastecer(self):
        print(f"{self.nome} abastecido com {self.combustivel}.")


class Motocicleta(Terrestre):
    def __init__(self, nome, capacidade, velocidade_max, cilindradas: int):
        super().__init__(nome, capacidade, velocidade_max, num_rodas=2)
        self.cilindradas = cilindradas

    def empinar(self):
        print(f"{self.nome} ({self.cilindradas}cc) empinando!")


class Onibus(Terrestre):
    def __init__(self, nome, capacidade, velocidade_max, num_assentos: int):
        super().__init__(nome, capacidade, velocidade_max, num_rodas=6)
        self.num_assentos = num_assentos

    def embarcar_passageiros(self):
        print(f"{self.nome}: embarcando passageiros ({self.num_assentos} assentos).")

class AviaoMonomotor(Aereo):
    def __init__(self, nome, capacidade, velocidade_max, altitude_max, prefixo: str):
        super().__init__(nome, capacidade, velocidade_max, altitude_max)
        self.prefixo = prefixo

    def decolar(self):
        print(f"{self.nome} (prefixo {self.prefixo}) decolando em pista curta!")


class AviaoComercial(Aereo):
    def __init__(self, nome, capacidade, velocidade_max, altitude_max,
                 num_motores: int, companhia: str):
        super().__init__(nome, capacidade, velocidade_max, altitude_max)
        self.num_motores = num_motores
        self.companhia = companhia

    def fazer_checkin(self):
        print(f"Check-in aberto para o voo da {self.companhia} — {self.nome} ({self.num_motores} motores).")

class Lancha(Aquatico):
    def __init__(self, nome, capacidade, velocidade_max, profundidade_max, potencia_hp: int):
        super().__init__(nome, capacidade, velocidade_max, profundidade_max)
        self.potencia_hp = potencia_hp

    def acelerar(self):
        print(f"{self.nome} acelerando a {self.velocidade_max}km/h com {self.potencia_hp}HP!")


class Navio(Aquatico):
    def __init__(self, nome, capacidade, velocidade_max, profundidade_max, tonelagem: float):
        super().__init__(nome, capacidade, velocidade_max, profundidade_max)
        self.tonelagem = tonelagem 

    def atracar(self):
        print(f"{self.nome} ({self.tonelagem:.0f} toneladas) atracando no porto.")
