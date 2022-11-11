from ConexaoBD import *
from Banco import *
user='a definir'
class Pessoa:
    def __init__(self):
        self._email = None
        self._senha = None
        self._telefone = None
        self._dict = {}   
        self._nm_user = user
        self._dataniver = user
# atributos usuario
    def AddUsuario(self):
        self._email  = input("Insira o email: ")
        self._senha= input("Insira a senha: ")
        self._telefone = input("Insira o telefone: ")
    def ConfirmaDado(self):
        x= input("Confirme o seu email: ")
        y= input("Confirme a sua senha: ")
        if self._email == x and self._senha == y:
            print("\033[0;49;32mTudo certo!")
            return 's'
        else:
            print("\033[0;49;31merro os dados digitados não coincidem")
            print('\033[1;94m')
            return 'n'
# metodo para confirmar dados        
    def AddDados(self):
      try:
       dadosusu = "INSERT INTO usuario (email,senha,nome_user,telefone,data_aniver) VALUES ('"+self._email+"','"+self._senha+"','"+self._nm_user+"','"+self._telefone+"','"+self._dataniver+"');" 
       insert(variconexao,dadosusu)
      
      except sqlite3.Error as e:
       print(e)




