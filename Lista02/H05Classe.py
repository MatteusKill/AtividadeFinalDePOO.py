class Pessoa:
    def __init__(self, nome: str, telefone: str, email: str, endereco: str):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def negociar(self):
        print(f"{self.nome} está iniciando uma negociação...")


class PessoaFisica(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: str, cpf: str):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf

    def assinar_contrato(self):
        print(f"{self.nome} (CPF: {self.cpf}) assinou o contrato.")


class PessoaJuridica(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, endereco: str,
                 cnpj: str, razao_social: str):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.razao_social = razao_social

    def emitir_nota_fiscal(self):
        print(f"Nota fiscal emitida por {self.razao_social} (CNPJ: {self.cnpj})")
