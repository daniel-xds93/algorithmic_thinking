valor_total = float(input("Digite o valor da compra: R$ "))

opcao_pgto = input('''Selecione a forma de pagamento: 
(B) - Boleto 
(C) - Cartão 
(D) - Dinheiro
Digite a opção desejada: ''')

valor_pagar = 0
# Boleto = 15%  e Dinheiro = 10% 
if opcao_pgto == 'B':
    valor_pagar = valor_total * 0.85

elif opcao_pgto == 'D':
    valor_pagar = valor_total * 0.9

else:
    valor_pagar = valor_total


print(f'Valor a pagar R$ {valor_pagar}')