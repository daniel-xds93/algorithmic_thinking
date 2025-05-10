
try:

    lista = ['Python', 'Java', 'C#', 'PHP']

    num = int(input("Digite um número: "))

    print(f'Linguagem escolhida: {lista[num]}')

except ValueError:
    print("Valor informado não é um número")

except IndexError:
    print('Número informado não está na lista')

except:
    print("Erro desconhecido!")