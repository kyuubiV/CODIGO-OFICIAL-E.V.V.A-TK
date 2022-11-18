from ConexaoBD import *
from Banco import *
user='a definir'
class Pessoa:
    def __init__(self,email,senha,telefone):
        self._email = email
        self._senha = senha
        self._telefone =telefone
        self._nm_user = user
        self._dataniver = user
# metodo para adicionar dados ao dicionario        
    def AddDados(self):
      try:
       dadosusu = "INSERT INTO usuario (email,senha,nome_user,telefone,data_aniver) VALUES ('"+self._email+"','"+self._senha+"','"+self._nm_user+"','"+self._telefone+"','"+self._dataniver+"');" 
       insert(variconexao,dadosusu)
      except sqlite3.Error as e:
       print(e)
    
    def Login(self):
        try:
         banco=select(variconexao,"SELECT * FROM usuario WHERE email ='"+self._email+"' AND senha ='"+self._senha+"'")
         if len(banco) == 1:
           return banco
         else:
           return banco
        except sqlite3.Error as e:
         print('algo deu errado',e)
        
    def AlterarSenha(self):
       banco=select(variconexao,"SELECT * FROM usuario WHERE email ='"+self._email+"' AND telefone ='"+self._telefone+"'")
       if len(banco) == 1:
        try:
          x=banco[0]
          banco2=update(variconexao,"UPDATE usuario SET senha ='"+self._senha+"' WHERE id_user ='"+x[0]+"';")
          return True
        except sqlite3.Error as e:
          print(e)
       else:
         return False

