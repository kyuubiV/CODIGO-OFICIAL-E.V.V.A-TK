from Pessoa import *
from ConexaoBD import *
from Banco import *
class User(Pessoa):
  
    def __init__(self,email,senha,telefone):
        super().__init__(email,senha,telefone)


    
# metodo para alterar a senha
    def ExibirDados(self,user):
        banco=select(variconexao,"SELECT * FROM usuario WHERE id_user ='"+str(user)+"';")
        return banco
# metodo para exibir os dados      
    def EditarDados(self,valor,user,x):
        if x == '1':
         try:
          update(variconexao,"UPDATE usuario SET nome_user ='"+valor+"' WHERE id_user ='"+user+"';")
          return True
         except sqlite3.Error as e:
          print(e)
        elif x == '2':
         try:
          update(variconexao,"UPDATE usuario SET telefone ='"+valor+"' WHERE id_user ='"+user+"';")
          return True
         except sqlite3.Error as e:
          print(e)
        elif x == '3':
         try:
          update(variconexao,"UPDATE usuario SET data_aniver ='"+valor+"' WHERE id_user ='"+user+"';")
          return True
         except sqlite3.Error as e:
          print(e)
        else:
            return False
# metodo para editar os dados do usuario