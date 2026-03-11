class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def alterar_editora(self, nova_editora):
        self.editora = nova_editora

    ## Método listar_qtde_paginas retorna o valor de páginas
    def listar_qtde_paginas(self):
        return self.paginas