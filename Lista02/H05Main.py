cores = {"limpa": "\033[m", "amarelo": "\033[33m"}

from H05Classe import PessoaFisica, PessoaJuridica

pf = PessoaFisica("Carlos Silva", "67 99999-0001", "carlos@email.com",
                  "Rua das Flores, 10", "123.456.789-00")
pf.negociar()
pf.assinar_contrato()

print()

pj = PessoaJuridica("Baikal Security", "67 3333-0001", "contato@baikal.com",
                    "Av. Afonso Pena, 500", "12.345.678/0001-99", "Baikal Segurança Ltda")
pj.negociar()
pj.emitir_nota_fiscal()
