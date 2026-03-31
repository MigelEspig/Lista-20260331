class Retangulo:
    def __init__(self, largura, altura):
        self.base = largura
        self.altura = altura
    def calcular_area(self):
        return self.base * self.altura
    
retanguloQualquer = Retangulo(5, 10)

def exibir_area():
    area = retanguloQualquer.calcular_area()
    print(f'Área do retângulo: {area}')

exibir_area()