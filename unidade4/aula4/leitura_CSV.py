
with open("indicacao_economica.csv", 'r') as arquivo:
    # a linha abaixo apresenta os dados do arquivo
    # print(arquivo.readlines()[1:-1])

    total_voos = float(0)
    maior =float(0)
    total_passageiros = float(0)
    maior_media_diaria = float(0)

    ano_usuario = input("Digite o ano desejado: ")

    for linha in arquivo.readlines()[1:-1]:
        lista = linha.split(',')
        total_voos += float(lista[3])

        if float(lista[2]) > float(maior):
            maior = lista[2]
            ano = lista[0]
            mes = lista[1]

        if ano_usuario == lista[0]:
            total_passageiros += float(lista[2])

            if float(lista[5]) > float(maior_media_diaria):
                maior_media_diaria = lista[5]
                mes_maior_media_diaria = lista[1]


    print(f"O total de voos é: {total_voos}")    
    print(f"O mês/ano de maior movimento foi: {mes}/{ano}")
    print(f"O total de passageiros no ano {ano_usuario} foi de {total_passageiros}")
    print(f"O mês do ano {ano_usuario} com maior média de hotel foi {maior_media_diaria}")
