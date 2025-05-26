
class Aluno():
    def __init__(self, nome_aluno, idade_aluno, email_aluno, nota1_aluno, nota2_aluno):
        self.nome = nome_aluno
        self.idade = idade_aluno
        self.email = email_aluno
        self.nota1 = nota1_aluno
        self.nota2 = nota2_aluno

    def media_aluno(self):
        return (self.nota1 + self.nota2) / 2
    
    def status_aluno(self):
        if self.media_aluno() >= 6.0:
            return "APROVADO"
        
        return "REPROVADO"
    
    # a função abaixo formata a saída do objeto
    def __str__(self):
        return f"Nome: {self.nome} - Idade: {self.idade} - Email: {self.email}"

# a linha abaixo instancia a classe
aluno1 = Aluno("Daniel Xavier", 32, "daniel@pro.fecaf.com.br", 6.3, 5.4)
aluno2 = Aluno("Vilma Nunes", 36, "vilma.nunes@a.fecaf.com.br", 8.6, 8.0)
aluno3 = Aluno("Isabella Nunes", 3, "isa.bella@a.fecaf.com.br", 8.7, 9.5)

lista_alunos = [aluno1, aluno2, aluno3]

for i, aluno in enumerate(lista_alunos):
    #print(f"#{i+1} - Nome: {aluno.nome} - Média: {aluno.media_aluno()} - Status: {aluno.status_aluno()}")
    print(aluno)

#print(aluno1)