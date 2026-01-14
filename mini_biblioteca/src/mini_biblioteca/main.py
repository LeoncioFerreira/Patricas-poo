from usuarios import Usuario 
from livros import Livro
from emprestimos import Emprestimo

usuario = Usuario("Leôncio","1")

livro = Livro("O conto do Leôncio","Leôncio","01")

print(f"Disponível: {livro.disponivel}")

emprestimo = Emprestimo(livro,usuario)

print(f"Empréstimo ativo: {emprestimo.ativo}")

Emprestimo.devolver(emprestimo)

print(f"Empréstimo ativo: {emprestimo.ativo}")
