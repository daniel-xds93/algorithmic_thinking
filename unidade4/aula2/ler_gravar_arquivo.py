
nome = input("Digite seu nome: ")
curso = input("Digite seu curso: ")

# a linha abaixo lê o arquivo .txt
with open('leitura.txt', 'r') as arquivo:
    dados = arquivo.read()

    # print(dados)

# a linha abaixo grava um arquivo .txt
with open('arquivo_escrito.txt', 'a') as arquivo:
    arquivo.write(f"Olá {nome}\n")
    arquivo.write(f"Seja bem-vindo(a) ao curso {curso}\n\n")