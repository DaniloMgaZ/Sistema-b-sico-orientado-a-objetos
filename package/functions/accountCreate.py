from package.dataBase.banco_de_dados import Dados

class Create:
    def __init__(self):
        pass

    def userInput(self):
        while True:
            user = input('Digite seu username: ').lower()
            if len(user) < 7:
                print('Mínimo 7 caracteres')
            else:
                if Dados('users').verificarUser(user) == True:
                    print('Esse username já existe, tente outro!.')
                else:
                    return user
            #Acrescentar mais coisa! tá no código systemcreate
    
    def passwordInput(self):
        password = True
        caracter = ['@', '#', '$', '!']
        while password:
            password = input('Digite sua senha: ')
            if len(password) < 7:
                print('Senha muito curta, mínimo 7 caracteres!.')
            else:
                for i, char in enumerate(password):
                    if not char in caracter:
                        teste = False
                    else:
                        teste = True
                        return password
                if teste == False:
                    print('Sua senha precisa ter algum caracter especial. (@, #, $, !)')