from ConexaoBD import *
from Banco import *
user='a definir'
class Pessoa:
    def __init__(self,email,senha,telefone):
        self._email = email
        self._senha = senha
        self._telefone =telefone
        self._dict = {}
        self._return = None
        self._nm_user = user
        self._dataniver = user
# metodo para adicionar dados ao dicionario        
    def AddDados(self):
      try:
       dadosusu = "INSERT INTO usuario (email,senha,nome_user,telefone,data_aniver) VALUES ('"+self._email+"','"+self._senha+"','"+self._nm_user+"','"+self._telefone+"','"+self._dataniver+"');" 
       insert(variconexao,dadosusu)
      except sqlite3.Error as e:
       print(e)
    
    def Login(self,email,senha):
        try:
         banco=select(variconexao,"SELECT * FROM usuario ORDER BY email ASC ")
         for Dados in banco:
           if email == Dados[1] and senha == Dados[2]:
             return True
             self._return = dados[0]
           elif email == Dados[1] and senha!= Dados[2]:
             return 'tl'
           else:
             return False
        except a:
         print('algo deu errado',a)
