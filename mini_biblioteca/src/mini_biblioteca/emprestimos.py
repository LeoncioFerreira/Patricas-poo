from livros import Livro
from usuarios import Usuario

class Emprestimo:
    def __init__(self, livro: Livro, usuario: Usuario, ativo: bool = True):
        if not livro.disponivel:
            raise ValueError(f"O livro '{livro.titulo}' não está disponível para empréstimo")
        
        self.livro = livro
        self.usuario = usuario
        self.ativo = ativo
        self.livro.disponivel = False

    def devolver(self):
        self.ativo = False
        self.livro.disponivel = True