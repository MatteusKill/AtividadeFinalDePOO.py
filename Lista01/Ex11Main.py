cores = {
    "limpa": "\033[m",
    "amarelo": "\033[33m"
}

from Ex11Classe import Nota_Fiscal

numero = int(input("Número da NF: "))
tipo = input("Tipo (Entrada/Saída): ")
serie = int(input("Série (1, 2 ou 3): "))
cnpj = input("CNPJ: ")
razao_social = input("Razão Social: ")
data = input("Data de emissão (dd/mm/aaaa): ")
valor_produtos = float(input("Valor dos produtos: R$ "))
icms = float(input("ICMS: R$ "))
frete = float(input("Frete: R$ "))
ipi = float(input("IPI: R$ "))

nf01 = Nota_Fiscal(numero, tipo, serie, cnpj, razao_social, data,
                   valor_produtos, icms, frete, ipi)

print(f"{cores['amarelo']}Número da NF:{cores['limpa']} {nf01.obter_numero()}")
print(f"{cores['amarelo']}Data de emissão:{cores['limpa']} {nf01.obter_data_emissao()}")

nova_razao = input("Informe nova razão social (ou Enter para manter): ")
if nova_razao.strip():
    nf01.alterar_razao_social(nova_razao)
    print(f"{cores['amarelo']}Razão social atualizada:{cores['limpa']} {nf01.razao_social}")

print(f"{cores['amarelo']}Valor total da NF:{cores['limpa']} R$ {nf01.calcular_valor_total():.2f}")
