from package.dataBase.banco_de_dados import Dados
from package.system.baseSystem import System

class SystemV(System):
    def __init__(self, user):
        super().__init__(user)
        self.opcoes = {
            '2': self.logout,
            '1': self.criarLoja
        }
        self.opcoesLoja = {
            '1': self.adicionarItem,
            '2': self.removerItem,
            '3': self.listarItens,
            '4': self.voltar
        }
        self.loja = Dados('vendedores').getLojaName(user)

    def criarLoja(self):
        item = {'item': None , 'price': None }
        if Dados(self.loja).existeLoja(self.loja) == True:
            self.minhaLoja()
        else:
            Dados('package/dataBase/db/lojas/' + self.loja).escrever(item)
            self.minhaLoja()

    def default(self):
        return True
    
    #system entregador
    def menu(self):
        while self.continuar:
            escolha = input(f'\n{self.name}, utilize, (1) - Minha Loja (2)- logout\n:')
            self.continuar = self.opcoes.get(escolha, self.default)()


    def logout(self):
        sair = input('Você deseja sair?\n: ')
        match sair:
            case 'sim':
                print('Até logo!.')
                self.continuar = False
            case 'nao':
                pass
            case _:
                print('Inválido')

    def minhaLoja(self):
        while self.continuar:
            escolha = input(f'\nA sua loja: {self.loja} está aberta, digite o que você deseja fazer\n(1)- Adicionar Item, (2)- Remover Item, (3)- Listar Itens, (4)- Voltar: ')
            self.opcoesLoja.get(escolha, self.default)()

    def adicionarItem(self):
        while True:
            item = input('\nDigite o nome do item\n: ')
            try:
                price = float(input('Digite o preço: '))
            except ValueError:
                print("Preço inválido. Por favor, insira um número válido.")
                continue
            store = {'item': item, 'price': price}
            dados = Dados('/lojas/'+ self.loja)
            dados.escreverV(store)
            sim = int(input('\nDigite (1) para adicionar mais itens ou (2) para voltar a sua loja\n:'))
            match sim:
                case 1:
                    self.adicionarItem()
                case 2:
                    self.minhaLoja()
                    return False
    
    def removerItem(self):
        Dados(self.loja).listar()
        remove = int(input('\nDigite qual posição deseja remover\n: '))
        Dados(self.loja).removerItem(remove)
        return True
    
    def listarItens(self):
        Dados(self.loja).listar()
        return True
    
    def voltar(self):
        self.menu()
        return False
