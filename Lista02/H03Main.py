cores = {"limpa": "\033[m", "amarelo": "\033[33m"}

from H03Classe import Ingresso, IngressoVIP

ingresso01 = Ingresso(80.00, "Pista")
ingresso01.mostrar_setor()
ingresso01.alterar_preco(90.00)

print()

vip01 = IngressoVIP(350.00, "Camarote Premium",
                    camarote=True, open_bar=True, open_food=False, estacionamento=True)
vip01.mostrar_setor()
vip01.pegar_bebida()
vip01.acessar_camarote()
