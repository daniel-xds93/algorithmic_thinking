
class Aluno():
    def __init__(self, nome_aluno, idade_aluno, email_aluno, nota1_aluno, nota2_aluno):
        self.nome = nome_aluno
        self.idade = idade_aluno
        self.email = email_aluno
        self.nota1 = nota1_aluno
        self.nota2 = nota2_aluno

# a linha abaixo instancia a classe
aluno1 = Aluno("Daniel Xavier", 32, "daniel@pro.fecaf.com.br", 6.3, 5.4)
aluno2 = Aluno("Vilma Nunes", 36, "vilma.nunes@a.fecaf.com.br", 8.6, 9.0)
aluno3 = Aluno("Isabella Nunes", 3, "isa.bella@a.fecaf.com.br", 8.7, 9.5)

lista_alunos = [aluno1, aluno2, aluno3]

for i, aluno in enumerate(lista_alunos):
    print(f"#{i+1} - Nome: {aluno.nome} - Idade: {aluno.idade}")