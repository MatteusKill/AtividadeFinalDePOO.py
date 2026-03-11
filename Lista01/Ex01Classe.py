##Classe Pessoa criada
class Pessoa:
    ## classe com construtor e atributos definidos para os objetos definidos
    def __init__(self, nome: str, idade: int,endereco: str):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    ## método para mostrar_nome
    def mostrar_nome(self):
        return self.nome
    
    ## método para alterar_idade
    def alterar_idade(self, alterar_idade):
        self.idade = alterar_idade
    
    ## método para imprimir_endereco
    def imprimir_endereco(self):
        return self.endereco