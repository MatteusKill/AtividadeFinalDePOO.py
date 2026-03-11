cores = {
    "limpa":"\033[m",
    "vermelho":"\033[31m",
    "amarelo":"\033[33m"
}

from Ex02Classe import Livro

nome_livro = input("Infomer o nome do livro: ")
autor_livro = input("Informe o nome do autor: ")
editora_do_livro = input("Informe o nome da editora que escreveu o livro: ")
qntd_paginas = int(input("Informe a quantidade de páginas que contem o livro: "))

livro01 = Livro(nome_livro, autor_livro, editora_do_livro, qntd_paginas)
print(f"{cores['amarelo']}O nome da editora responsável pelo livro eh: {cores['limpa']}")
print(livro01.editora)

nova_editora = input("Informe o nome da nova editora: ")
livro01.alterar_editora(nova_editora)
print(f"{cores['amarelo']}Novo nome da editora:{cores['limpa']}")
print(livro01.editora)

print(f"{cores['amarelo']}Listando a quantidades de páginas do livro: {cores['limpa']}")
print(livro01.listar_qtde_paginas())