from package.dataBase.banco_de_dados import Dados
from package.system.baseSystem import System

class SystemU(System):
    def __init__(self, user):
        super().__init__(user)
        self.opcoes = {
            '1': self.encontrarLojas,
            '2': self.logout
        }
        self.acessar = {
            '1': self.entrarLoja,
            '2': self.menu
        }

    def default(self):
        return True
    
    #system entregador
    def menu(self):
        while self.continuar:
            escolha = input(f'{self.name} utilize, (1) - Encontrar Lojas, (2)- logout \n:')
            self.continuar = self.opcoes.get(escolha, self.default)()

    def encontrarLojas(self):
        while self.continuar:
            escolha = input('(1) - Entrar em uma loja, (2) - Voltar para o Menu \n:')
            self.continuar = self.acessar.get(escolha, self.default)()

    def entrarLoja(self):
        Dados('vendedores').listarLojas()
        while True:
            try:
                digitar = int(input('\nDigite qual loja você deseja entrar.\n(0) - Para retornar ao menu\n: '))
                if digitar == 0:
                    self.menu()
                    break
                else:
                    variavel = Dados('vendedores').entrarLojas(digitar)
                    Dados('/lojas/' + variavel).viewLoja()
                    self.loja(variavel)
                    return False
            except:
                print('Essa loja não existe!.')
    
    def loja(self,variavel):
        status = 'não está em rota de entrega'
        while True:
            digitar = int(input('\nDigite o item que você deseja comprar\n: '))
            digitar-=1
            price, name = Dados('/lojas/' + variavel).comprarLoja(digitar)
            if name is not None and price is not None:
                lista = {'comprador': self.name,'item': name, 'price': price, 'status': status}
                Dados('/pedidos/'+ self.name).escreverV(lista)
                print(f'Você comprou {name} pelo valor de {price}. A entrega acontecerá em breve!.')
                return False
            else:
                print('Não existe')

    def logout(self):
        sair = input('Você deseja sair?\nDigite (sim) ou (nao)\n: ')
        match sair:
            case 'sim':
                print('Até logo!.')
                self.continuar = False
            case 'nao':
                pass
            case _:
                print('Inválido')