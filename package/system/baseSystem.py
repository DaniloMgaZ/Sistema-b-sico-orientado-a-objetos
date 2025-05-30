from package.dataBase.banco_de_dados import Dados
from abc import ABC, abstractmethod

class System(ABC):
    def __init__(self,user):
        self.user = user
        self.name = Dados('users').getName(user)
        self.continuar = True
        self.opcoes = {}

    @abstractmethod
    def menu(self):
        pass

    def logout(self):
        sair = input('Você deseja sair?\n: ')
        match sair.lower():
            case 'sim':
                print('Até logo!')
                self.continuar = False
            case 'não' | 'nao':
                pass
            case _:
                print('Opção inválida.')