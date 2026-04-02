class Animal:
    def __init__(self,nome):
        self.nome = nome
    def emitir_som(self):
        return "*som foda de um animal qualquer*"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!!!!!"

gatoFudido = Gato("Romualdo")
print(f"{gatoFudido.nome} faz {gatoFudido.emitir_som()}")