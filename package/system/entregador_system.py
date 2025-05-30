from package.dataBase.banco_de_dados import Dados
from package.system.baseSystem import System
from inputimeout import inputimeout, TimeoutOccurred
import random

class SystemE(System):
    def __init__(self, user):
        super().__init__(user)
        self.opcoes = {
            '1': self.entregador,
            '2': self.logout
        }
        self.opcoes_f = {
            '1': self.buscarEntregas,
            '2': self.iniciarEntrega,
            '3': self.voltar
        }

    def default(self):
        return True
    
    #system entregador
    def menu(self):
        while self.continuar:
            escolha = input(f'{self.name} utilize, (1) - Entregador, (2)- logout\n:')
            self.continuar = self.opcoes.get(escolha, self.default)()

    def voltar(self):
        return False
    
    def entregador(self):
        while self.continuar:
            escolha = input('Utilize, (1) - Buscar Entregas, (2) - Iniciar Entrega, (3) - Voltar\n:')
            self.continuar = self.opcoes_f.get(escolha, self.default)()

    def buscarEntregas(self):
        pedidos = '/pedidos/'
        entregas_entregador = Dados('/entregadores/' + self.name).dataBase
        if entregas_entregador:
            print("Você já tem uma entrega pendente. Finalize-a antes de pegar uma nova.")
            return True
        teste = Dados(pedidos).buscarEnt()
        try:
            escolha = int(input("\nDigite o número do pedido que deseja visualizar: "))
            if 1 <= escolha <= len(teste):
                nome_arquivo, pedido = teste[escolha - 1]
                print(f"\n📦 Pedido: {nome_arquivo}")
                Dados(pedidos).exibirPedido(pedido)
                escolher = input('Digite (sim), caso deseja pegar essa entrega: ').lower()
                if escolher == 'sim':
                    name, nameItem, priceItem = Dados(nome_arquivo).pegarPedido()
                    lista = {'Cliente': name,'Item': nameItem, 'price': priceItem}
                    Dados('/entregadores/' + self.name).escrever(lista)
                    Dados(nome_arquivo).saiuEntrega(name,nameItem,priceItem)
                    print('A entrega foi adicionada em sua lista!.')
            else:
                print("Número inválido.")
        except TypeError or ValueError:
            print("Entrada inválida.")
        return True
        
    def iniciarEntrega(self):
        exist = Dados(self.name).verificarEntrega()
        if exist == True:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            x = a * b
            gorjeta = random.randint(1,20)
            print(f"\nQuanto é: {a} * {b}? (Você tem 10 segundos para responder)")
            try:
                resposta = int(inputimeout(prompt='Resposta: ', timeout=10))
                if resposta == x:
                    print("✅ Entrega realizada com sucesso!.")
                    print(f'Você ganhou uma gorjeta de + R${gorjeta}!.')
                    print(f'Valor entrega: R$30,00 + R${gorjeta} = R${30+gorjeta}')
                    cliente = Dados(self.name).getCliente()
                    Dados(cliente).remover(cliente)
                    Dados(self.name).removerE(self.name)
                    self.menu()
                else:
                    print(f"❌ Errou o caminho e atrasou o pedido!. A resposta era {x}")
                    print(f'Você não recebeu gorjeta!. R$30,00')
                    Dados(cliente).remover(cliente)
                    Dados(self.name).remover(self.name)
                    self.menu()
            except ValueError:
                print("\n⚠️ Entrada inválida! Só pode números.")
            except TimeoutOccurred:
                print(f"❌ Errou o caminho e atrasou o pedido!. A resposta era {x}")
                print(f'Você não recebeu gorjeta!. R$30,00')
                Dados(cliente).remover(cliente)
                Dados(self.name).remover(self.name)
                self.menu()
        else:
            print('\n Você ainda não pegou uma entrega!.')
            self.menu()

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