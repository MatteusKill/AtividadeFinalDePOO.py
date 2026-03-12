cores = {
    "limpa": "\033[m",
    "amarelo": "\033[33m"
}

from Ex10Classe import Carro

modelo = input("Informe o modelo do carro: ")
marca = input("Informe a marca: ")
cor = input("Informe a cor: ")
ano = int(input("Informe o ano: "))
valor = float(input("Informe o valor do carro: R$ "))
consumo = float(input("Informe o consumo (km/L): "))

carro01 = Carro(modelo, marca, cor, ano, valor, consumo)

litros = float(input("Quantos litros deseja abastecer? "))
carro01.abastecer(litros)

distancia = float(input("Quantos km deseja percorrer? "))
carro01.andar(distancia)

print(f"{cores['amarelo']}Verificando nível:{cores['limpa']}")
carro01.verificar_nivel()

print(f"{cores['amarelo']}IPVA (2,5%):{cores['limpa']} R$ {carro01.calcular_imposto():.2f}")
