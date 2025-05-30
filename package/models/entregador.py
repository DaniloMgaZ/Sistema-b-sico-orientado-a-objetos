from package.models.pessoas import Pessoas

class Entregador(Pessoas):
    def __init__(self, nome, veiculo, idade):
        super().__init__(nome, idade)
        self.veiculo = veiculo
    
    def __str__(self):
        return f'Parabéns, {self.nome}, sua conta foi criada como Entregador.\n Que suas entregas sejam realizadas com segurança, junto com seu veíiculo: {self.veiculo}'
    