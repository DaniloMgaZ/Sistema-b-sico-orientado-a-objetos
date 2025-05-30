import json
import os

class Dados:
    def __init__(self, tipo_de_dados):
        self.db_file_name = 'package/dataBase/db/' + tipo_de_dados + '.json'
        self.dataBase = []
        self.tipo_de_dados = tipo_de_dados
        self.ler()

    def ler(self):
        try:
            with open(self.db_file_name, 'r') as file:
                self.dataBase = json.load(file)
        except (FileNotFoundError , json.JSONDecodeError):
            self.dataBase = []

    def escrever(self, x):
        try:
            for i, user in enumerate(self.dataBase):
                if user['user'] == x['user']:
                    self.dataBase[i] = x
                    break
            else:
                self.dataBase.append(x)
            with open(self.db_file_name, 'w') as file:
                json.dump(self.dataBase, file, indent=4, ensure_ascii=False)
        except Exception:
            return

    # USERS
    def verificarUser(self, user):
        for userGet in self.dataBase:
            if user == userGet['user']:
                return True
        return False
    
    def validarCriacao(self, user):
        for nameGet in self.dataBase:
            if user == nameGet['user']:
                if nameGet['status'] == '' and nameGet['idade'] == 0 and nameGet['name'] == '':
                    return True
        return False
    
    def finalizarCriacao(self, user,name,idade,status):
        for findUser in self.dataBase:
            if user == findUser['user']:
                findUser.update({'name': name, 'idade': idade,'status': status})
                self.escrever(findUser)
                return
        print('Houve um erro!.')

    def getName(self, user):
        for findName in self.dataBase:
            if user == findName['user']:
                x = findName['name']
                return x
        print('erro')
        return None

    
    def verificarLogin(self, user, password):
        for loginGet in self.dataBase:
            if user == loginGet['user'] and password == loginGet['password']:
                return True
        return False
    #-------------------------------------------------#
    #system
    def type_account(self, user):
        for findUser in self.dataBase:
            if user == findUser['user']:
                if findUser['status'] == 'usuario':
                    return 'usuario'
                elif findUser['status'] == 'entregador':
                    return 'entregador'
                else:
                    return 'vendedor'
    #------------------------------------------------------#
    #vendedor
    def getLojaName(self, user):
        for getLoja in self.dataBase:
            if user == getLoja['user']:
                loja = getLoja['loja']
                return loja
        print('Loja não existe.')
    
    def existeLoja(self, loja):
        for loja in self.dataBase:
            if loja:
                return True
        return False
    
    def escreverV(self, x):
        try:
            self.dataBase.append(x)
            with open(self.db_file_name, 'w', encoding='utf-8') as file:
                json.dump(self.dataBase, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f'Erro ao escrever no banco de dados: {e}')

    def listar(self):
        try:
            i = 0
            with open('package/dataBase/db/lojas/' + self.tipo_de_dados + '.json', 'r') as file:
                self.dataBase = json.load(file)
                print(self.tipo_de_dados)
        except FileNotFoundError:
            print('Arquivo não encontrado')
            return
        except json.JSONDecodeError:
            print('Erro ao ler o arquivo JSON.')
            return
        if not self.dataBase:
            print('Loja está vazia!.')
        else:
            print(self.tipo_de_dados)            
            for item in self.dataBase:
                i+=1
                print(f'{i} Nome: ',item['item'], 'Preço', item['price'])
            return

    def removerItem(self, remove):
        with open('package/dataBase/db/lojas/' + self.tipo_de_dados + '.json', 'r') as file:
            self.dataBase = json.load(file)
        remove -= 1
        temporary = self.dataBase[remove]
        item = temporary.get('item')
        del self.dataBase[remove]
        with open('package/dataBase/db/lojas/' + self.tipo_de_dados + '.json', 'w') as file:
            json.dump(self.dataBase, file, indent=4, ensure_ascii=False)
        print(f'O item {item} foi removido')

    #Usuario
    def listarLojas(self):
        try:
            with open(self.db_file_name, 'r') as file:
                self.dataBase = json.load(file)
            lojas = [vendedor['loja'] for vendedor in self.dataBase if vendedor.get('loja')]
            for idx, loja in enumerate(lojas, start=1):
                print(f"{idx}. {loja}")
        except:
            return

    def entrarLojas(self, number):
        try:
            with open(self.db_file_name, 'r') as file:
                self.dataBase = json.load(file)
            lojas = [vendedor['loja'] for vendedor in self.dataBase if vendedor.get('loja')]
            for idx, loja in enumerate(lojas, start=1):
                print(f"{idx}. {loja}")
            print(lojas[number-1])
            temporary = lojas[number-1]
            return temporary
        except:
            return
        
    def viewLoja(self):
        try:
            i = 0
            with open(self.db_file_name, 'r') as file:
                self.dataBase = json.load(file)
            for item in self.dataBase:
                i+=1
                print(f'{i}Nome: ',item['item'], 'Preço', item['price'])
        except:
            print('A loja ainda não foi inaugurada!.')

    def comprarLoja(self, temp):
        with open(self.db_file_name, 'r') as file:
            self.dataBase = json.load(file)
        try:
            item = self.dataBase[temp]
            catName = item['item']
            catPrice = item['price']
            return catPrice, catName
        except:
            return None, None
        

    #ENTREGADOR
    def buscarEnt(self):
        pedidos_path = 'package/dataBase/db/pedidos/'
        arquivos_validos = []
        if not os.path.isdir(pedidos_path):
            print(f'A pasta {pedidos_path} não existe')
            return
        print(f'Pedidos disponíveis:\n')
        for i, arquivo in enumerate(os.listdir(pedidos_path)):
            if arquivo.endswith('.json'):
                caminho = os.path.join(pedidos_path, arquivo)
                try:
                    with open(caminho, 'r', encoding='utf-8') as f:
                        dados = json.load(f)
                        arquivos_validos.append((arquivo, dados))
                        print(f"{i + 1}. {arquivo}")
                except (json.JSONDecodeError, FileNotFoundError):
                    print(f"Erro ao ler o arquivo {arquivo}")
        if not arquivos_validos:
            print("Nenhum pedido válido encontrado.")
            return
        return arquivos_validos
        

    def exibirPedido(self, pedido):
        if isinstance(pedido, list):
            print("Pedido:")
            for item in pedido:
                nome = item.get('price', 'Desconhecido')
                preco = item.get('item', 'N/A')
                print(f"  Produto: {nome} - Preço: R${preco}")
            print("-" * 40)
        elif isinstance(pedido, dict):
            itens = pedido.get('itens')
            if isinstance(itens, list):
                print("Pedido:")
                for item in itens:
                    nome = item.get('price', 'Desconhecido')
                    preco = item.get('item', 'N/A')
                    print(f"  Produto: {nome} - Preço: R${preco}")
                print("-" * 40)
            else:
                nome = pedido.get('price', 'Desconhecido')
                preco = pedido.get('item', 'N/A')
                print(f"  Produto: {nome} - Preço: R${preco}")
                print("-" * 40)

    def pegarPedido(self):
        with open('package/dataBase/db/pedidos/' + self.tipo_de_dados, 'r') as file:
            self.dataBase = json.load(file)
        for item in self.dataBase:
            name = item['comprador']
            nameItem = item['item']
            priceItem = item['price']
        return name,nameItem,priceItem

    def saiuEntrega(self, name, nameItem, priceItem):
        caminho_arquivo = 'package/dataBase/db/pedidos/' + self.tipo_de_dados
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            self.dataBase = json.load(file)
        atualizado = False
        for status in self.dataBase:
            if status.get('status') == 'não está em rota de entrega':
                status.update({'comprador': name,'item': nameItem,'price': priceItem,'status': 'está em rota de entrega.'})
                atualizado = True
                break
        if atualizado:
            with open(caminho_arquivo, 'w', encoding='utf-8') as file:
                json.dump(self.dataBase, file, indent=4, ensure_ascii=False)
            self.escreverV(status)
        else:
            print("Nenhum pedido foi atualizado.")
    
    def remover(self, arquivo):
        caminho = 'package/dataBase/db/pedidos/' + arquivo + '.json'
        try:
            os.remove(caminho)
        except:
            return 
    def removerE(self, arquivo):
        caminho = 'package/dataBase/db/entregadores/' + arquivo + '.json'
        try:
            os.remove(caminho)
        except:
            return
        
    def verificarEntrega(self):
        try:
            with open('package/dataBase/db/entregadores/' + self.tipo_de_dados + '.json') as file:
                self.dataBase = json.load(file)
                return True
        except FileExistsError:
            return False
        except:
            return False
        
    def getCliente(self):
        with open('package/dataBase/db/entregadores/' + self.tipo_de_dados + '.json') as file:
            self.dataBase = json.load(file)
        for cliente in self.dataBase:
            getCliente = cliente['Cliente']
        return getCliente