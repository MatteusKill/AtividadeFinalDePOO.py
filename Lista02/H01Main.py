cores = {"limpa": "\033[m", "amarelo": "\033[33m"}

from H01Classe import Acao, Drama, Suspense

filme_acao = Acao("Missão Impossível", 147, 32)
filme_acao.play()
filme_acao.explodir()

print()

filme_drama = Drama("Forrest Gump", 142, "superação e amor")
filme_drama.play()
filme_drama.chorar()

print()

filme_suspense = Suspense("Clube de Compras Dallas", 117, 8)
filme_suspense.play()
filme_suspense.revelar_vilao()
