class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2
    
alunoQualquer = Aluno('Erick', 6.0, 6.0)

def exibir_media():
    media = alunoQualquer.calcular_media()
    if media >= 6.0:
        print(f'Aluno {alunoQualquer.nome} aprovado com média {media:.2f}')
    else:
        print(f'Aluno {alunoQualquer.nome} reprovado com média {media:.2f}')

exibir_media()