
with open("pagina_gerada.html", "w") as pagina:
    pagina.write("<body><h2>Lista de Liguagens de programação</h2>")
    pagina.write("<h3>Lista que o usuario vai interagir:</h3>") 

    # a linha abaixo cria uma lista
    pagina.write("<ul>")

    linguagem = ''

    while linguagem != 'S' and linguagem != 's':

        linguagem = input("Digite a linguagem de programação ou S para Sair: ")

        if linguagem != "S" and linguagem != "s":
            pagina.write(f"<li>{linguagem}</li>")

    pagina.write("</ul></body>")