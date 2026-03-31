class livro:
    def __init__(self, titulo, autor, numPag):
        self.titulo = titulo
        self.autor = autor
        self.numPag = numPag

livroQualquer = livro('Dom Quixote', 'Miguel de Servantes', 280)

def lerLivro():
    print(f'Você está lendo o livro {livroQualquer.titulo}, do autor {livroQualquer.autor} e ele possui {livroQualquer.numPag} páginas.')

lerLivro()