from package.functions.accountInputName import inputName
from package.system.entregador_system import SystemE
from package.system.usuario_system import SystemU
from package.system.vendedor_system import SystemV
from package.dataBase.banco_de_dados import Dados

class SystemFunctions:
    def __init__(self):
        pass

    def verificacao(self, user):
        nFoiCriado = Dados('users').validarCriacao(user)
        if nFoiCriado:
            sucesso = inputName(user).createName(user)
            if sucesso:
                print('Conta criada!.')
                self.type_acount(user)
        self.type_acount(user)
    
    def type_acount(self,user):
        determinar = Dados('users').type_account(user)
        if determinar == 'usuario':
            SystemU(user).menu()
        elif determinar == 'vendedor':
            SystemV(user).menu()
        else:
            SystemE(user).menu()