from ConexaoBD import *
from Banco import *
user='a definir'
class Pessoa:
    def __init__(self,email,senha,telefone):
        self._email = email
        self._senha = senha
        self._telefone = telefone
        self._dict = {}   
        self._nm_user = user
        self._dataniver = user
# metodo para confirmar dados        
    def AddDados(self):
      try:
       dadosusu = "INSERT INTO usuario (email,senha,nome_user,telefone,data_aniver) VALUES ('"+self._email+"','"+self._senha+"','"+self._nm_user+"','"+self._telefone+"','"+self._dataniver+"');" 
       insert(variconexao,dadosusu)
       res = select(variconexao,'SELECT * FROM usuario')
       print(res)
      
      except sqlite3.Error as e:
       print(e)

# metodo para adicionar dados ao dicionario
      
    def Login(self):
        a = input('Digite seu email: ')
        b = input("Digite sua senha: ")
        try:
         y = self._dict[a]
        except:
         print('\033[0;49;31mnão existe usuario ',a)
        if a in self._dict.keys() and y[1] == b:
            print('\033[0;49;32mtudo certo')
            return a
        else:
            print("\033[0;49;31merro senha incorreta")
            print('\033[1;33m')
            return 'n'



