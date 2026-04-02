class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazerAniversario(self):
        self.idade += 1
        print(f'Parabéns {self.nome}! Agora você tem {self.idade} anos.')

pessoaQualquer = Pessoa('Erick', 17)
pessoaQualquer.fazerAniversario()
pessoaQualquer.fazerAniversario()

print(f"A pessoa {pessoaQualquer.nome} tem {pessoaQualquer.idade} anos.")