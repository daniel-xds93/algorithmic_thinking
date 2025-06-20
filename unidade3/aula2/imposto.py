
from calculossss import *

valor_produto = float(input("Digite o valor do produto: "))

estado = input("Digite a sigla do estado: ").upper()

empresa_estrangeira = input("A empresa é estrangeira? (S) Sim | (N) Não: ").upper()

print(f"""
Valor do produto R$ {valor_produto}
Valor do PIS R$ {calcular_PIS(valor_produto)}
Valor do COFINS R$ {calcular_COFINS(valor_produto)}
Valor do ISS R$ {calular_ISS(valor_produto, estado)}
Valor do ICMS R$ {calcular_ICMS(valor_produto, empresa_estrangeira)}

Valor total R$ {
    calcular_valor_total(valor_produto, calcular_PIS(valor_produto), 
                         calcular_COFINS(valor_produto), 
                         calular_ISS(valor_produto, estado), 
                         calcular_ICMS(valor_produto, empresa_estrangeira))
}
""")

