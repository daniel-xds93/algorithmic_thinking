
lista_alunos = ['Vilma', 'Alice', 'Isabella', 'Renan']

aluno_inserido = input("Digite o nome do aluno: ")

terceiro_aluno = input("Digite o nome que você quer inserir na 3ª posição: ")

# a linha abaixo adiciona um item no final da lista
lista_alunos.append(aluno_inserido)

# a linha abaixo insere o item em uma determinada posição
lista_alunos.insert(2, terceiro_aluno)

print(lista_alunos)

# a linha abaixo exclui um item da lista
lista_alunos.pop(1)

for aluno in lista_alunos:
    print(f'Nome: {aluno}')


total_alunos = len(lista_alunos)
print(f'Total de alunos = {total_alunos}')

posicao_aluno = lista_alunos.index("Isabella")

print(f'Posição do aluno na função index = {posicao_aluno}')

