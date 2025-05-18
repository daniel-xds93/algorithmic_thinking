
valor_produto = float(input("Digite o valor do produto: "))

# Abaixo ficam as constantes
PIS = valor_produto * 0.0165

COFINS = valor_produto * 0.076

estado = input("Digite a sigla do estado: ").upper()

ISS = 0.0

if estado == 'SP':
    ISS = valor_produto *0.03

elif estado == 'BA':
    ISS = valor_produto * 0.04

elif estado == 'RS':
    ISS = valor_produto * 0.05

else:
    ISS = valor_produto * 0.02

empresa_estrangeira = input("A empresa é estrangeira? (S) Sim | (N) Não: ").upper()

ICMS = 0.0

if empresa_estrangeira == 'S':
    ICMS = valor_produto * 0.04

else:
    ICMS = valor_produto * 0.1


valor_total = valor_produto + PIS + COFINS + ISS + ICMS

print(f"""
Valor do produto R$ {valor_produto}
Valor do PIS R$ {PIS}
Valor do COFINS R$ {COFINS}
Valor do ISS R$ {ISS}
Valor do ICMS R$ {ICMS}

Valor total R$ {valor_total}
""")