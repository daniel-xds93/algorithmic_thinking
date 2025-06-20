# a linha abaixo importa a biblioteca socket
import socket

lista_site = []
lista_ip = []

cont = ''

while cont != "N":
    url = input("Digite o site: ")

    ip = socket.gethostbyname(url)

    nome_site = url.split('.')

    lista_site.append(nome_site[1])
    lista_ip.append(ip)

    cont = input("Deseja continuar cadastrando? (S) Sim | (N) Não: ")


for i, site in enumerate(lista_site):
    print(f"Site: {site} - IP: {lista_ip[i]}")


#print(f"O IP do site {url} é: {ip}")
