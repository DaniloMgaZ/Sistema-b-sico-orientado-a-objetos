from package.dataBase.banco_de_dados import Dados
from package.controlls.main import *
from package.system.systemFunctions import SystemFunctions

class Login:
    def __init__(self):
        pass

    def loged(self, user):
        logado = True
        while logado:
            logado = SystemFunctions().verificacao(user)
        return False
    
    def loginVerify(self, user, password):
         if Dados('users').verificarLogin(user,password) == True:
              return True
         return False

    def login(self):
        logado = True
        while logado:
            user = input('Digite seu usuário: ').lower()
            password = input('Digite a sua senha: ')
            if self.loginVerify(user,password) == True:
                print('\nAcesso permitido!.\n')
                logado = self.loged(user)
                break
            else:
                print('Senha ou usuário errado.')