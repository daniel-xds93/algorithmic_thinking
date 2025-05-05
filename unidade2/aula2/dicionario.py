
veiculos = {
    'DMF-2230':['Gol', 'VW', 'Preto'],
    'FKL-7402':['Fiesta', 'Ford', 'Prata'],
    'GHZ-8229':['Onix', 'GM', 'Vermelho']
}

# a linha abaixo busca um veículo especifico
# print(veiculos.get('GHZ-8229'))

veiculos['DMF-3230'] = ['Sandero', 'Renault', 'Prata']

#print("Veículos cadastrados")
#print(veiculos)

# retornando apenas as chaves do dicionario
#print(veiculos.keys())

# a linha abaixo retorna apenas os valores do dicionario
#print(veiculos.values())

placa = input("Digite a placa do veículo: ")
modelo = input("Digite o modelo do veículo: ")
marca = input("Digite a marca do veículo: ")
cor = input("Digite a cor do veículo: ")

veiculos[placa] = [modelo, marca, cor]


for chave, dado in veiculos.items():
    print(f'Placa.............{chave}')
    print(f'Modelo............{dado[0]}')
    print(f'Marca.............{dado[1]}')
    print(f'Cor...............{dado[2]}')
    print()