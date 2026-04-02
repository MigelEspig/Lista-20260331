class Calculadora:
    def somar(self, a, b):
        return a + b
    def subtrair(self, a, b):
        return a - b
    def multiplicar(self, a, b):
        return a * b
    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Erro"

calculadora = Calculadora()

print(f'A soma de 10 e 5 é {calculadora.somar(10, 5)}')
print(f'A subtração de 10 e 5 é {calculadora.subtrair(10, 5)}')
print(f'A multiplicação de 10 e 5 é {calculadora.multiplicar(10, 5)}')
print(f'A divisão de 10 e 5 é {calculadora.dividir(10, 5)}')