from package.models.user import Usuario
from package.dataBase.banco_de_dados import Dados
from package.models.entregador import Entregador
from package.models.vendedor import Vendedor

class inputName(Usuario):
    def __init__(self, user):
        self.user = user
        
    def createName(self, user):
        name = str(input('\n Finalização de criação de conta.\nDigite seu nome: '))
        idade = int(input('Digite sua idade: '))
        tAccount = self.choiceType(user, name, idade)
        return True
    
    def choiceType(self, user, name, idade):
        escolher = True
        while escolher:
            tAccount = int(input('\nEscolha o tipo de conta\n(1) - Usuário. (2) - Entregador. (3) - Vendedor\n: '))
            match tAccount:
                case 1:
                    usuario = 'usuario'
                    Dados('users').finalizarCriacao(user, name, idade, usuario)
                    teste = {'user': user, 'name': name, 'idade': idade}
                    Dados('usuarios').escrever(teste)
                    return Usuario(name,idade)
                case 2:
                    entregador = 'entregador'
                    veiculo = str(input('Digite seu veículo: '))
                    Dados('users').finalizarCriacao(user,name, idade, entregador)
                    teste = {'user': user, 'name': name, 'idade': idade, 'veiculo': veiculo, 'entregas': 0}
                    Dados('entregadores').escrever(teste)
                    return Entregador(name,veiculo,idade)
                case 3:
                    vendedor = 'vendedor'
                    loja = input('Digite o nome de sua Loja: ')
                    Dados('users').finalizarCriacao(user,name,idade,vendedor)
                    teste = {'user': user, 'name': name, 'idade': idade, 'loja': loja}
                    Dados('vendedores').escrever(teste)
                    return Vendedor(name,idade,loja)
                case _:
                    print('Não existe!.')