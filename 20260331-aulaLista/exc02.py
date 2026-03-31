class Cachorro():
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca
    def Latir(self):
        print('Au Au!')

cachorroQualquer = Cachorro('Rex', 'Labrador')

def cachorroDoDiabo():
    print(f'nome: {cachorroQualquer.nome}')
    print(f'raça: {cachorroQualquer.raca}')
    cachorroQualquer.Latir()

cachorroDoDiabo()