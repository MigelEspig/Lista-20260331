class produto:
    def __init__(self,nome,preço,quantidade_em_estoque):
        self.nome = nome
        self.preço = preço
        self.quantidade_em_estoque = quantidade_em_estoque
    def  calcular_valor_total(self):
        valor_total = self.preço * self.quantidade_em_estoque
        print(f'O valor total do estoque de {self.nome} é R${valor_total:.2f}')
produtoQualquer = produto('Teclado', 100.00, 5)

produtoQualquer.calcular_valor_total()