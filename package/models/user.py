from package.models.pessoas import Pessoas

class Usuario(Pessoas):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    
    def __str__(self):
        return f'Parabéns, {self.nome}, sua conta foi criada como usuário!.'