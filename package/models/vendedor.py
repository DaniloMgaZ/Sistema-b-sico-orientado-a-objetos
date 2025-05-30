from package.models.pessoas import Pessoas

class Vendedor(Pessoas):
    def __init__(self, nome, idade, loja):
        super().__init__(nome, idade)
        self.loja = loja

    def __str__(self):
        return f'Parabéns, {self.nome}, sua conta foi criada como Vendedor.'