
def conversor(valor_em_dolar, valor_dolar_atual):
    return valor_em_dolar * valor_dolar_atual



dolar = float(input("Digite quantos dolares você possui $ "))

valor_dolar = float(input("Digite o valor do dolar no momento R$ "))

valor_convertido = conversor(dolar, valor_dolar)

print(f"valor em reais R$ {valor_convertido}")


print(f"Valor do conversor com outros parametros {round(conversor(5.00, 5.69), 2)}")