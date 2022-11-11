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
      
      except sqlite3.Error as e:
       print(e)




