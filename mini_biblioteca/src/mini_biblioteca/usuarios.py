
class Usuario:
    def __init__(self, nome:str, id_usuario:str):
        self.nome = nome
        self.id_usuario = id_usuario

    def cria_usuario(self,nome,id_usuario):
        Usuario = (nome,id_usuario)
        return Usuario
        