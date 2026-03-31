class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
carroQualquer = Carro('Fiat', 'Palio', 2010)

def exibir_detalhes():
    print(f'Marca: {carroQualquer.marca}')
    print(f'Modelo: {carroQualquer.modelo}')
    print(f'Ano: {carroQualquer.ano}')

exibir_detalhes()