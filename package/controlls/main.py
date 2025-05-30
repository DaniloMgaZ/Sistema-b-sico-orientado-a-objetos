from package.functions.accountCreate import Create
from package.dataBase.banco_de_dados import Dados
from package.functions.loginAccount import Login

class Main(Create,Dados):
    def __init__(self):
        super().__init__()
        self.opcoes = {
            '1': self.criarConta,
            '2': self.logarConta,
        }
        self.continuar = True
    
    def default(self):
        print('\n Não existe\n')
        return True
    
    def menu(self):
        while self.continuar:
            escolha = input('\nDigite (1) - Criar, (2) - Entrar \n: ')
            self.continuar = self.opcoes.get(escolha, self.default)()

    def criarConta(self):
        while True:
            name = ''
            idade = 0
            status = ''
            user = Create.userInput(self)
            Dados('users').verificarUser('user')
            password = Create.passwordInput(self)
            self.users = {'user': user, 'password': password, 'name': name, 'idade': idade, 'status': status}
            Dados('users').escrever(self.users)
            print('\nConta criada com sucesso!.')
            break
        self.menu()
    
    def logarConta(self):
        Login().login()
