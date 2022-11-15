from Pessoa import *
from ConexaoBD import *
from Banco import *
class User(Pessoa):
  
    def __init__(self):
        super().__init__()

# metodo que autoriza o usuario a entrar no planner
          
    def AlterarSenha(self,newsenha,user,telefone):
      banco=select(variconexao,"SELECT * FROM usuario WHERE id_user ='"+self._return+"';")
      for Dados in banco:
       if telefone == Dados[3]:
        try:
          update(variconexao,"UPDATE usuario SET email ='"+valor+"' WHERE id_user ='"+self._return+"';")
          return True
        except sqlite3.Error as e:
          print(e)
       else:
         return False
# metodo para alterar a senha
    def ExibirDados(self, val):
        banco=select(variconexao,"SELECT * FROM usuario WHERE id_user ='"+self._return+"';")
        return banco
# metodo para exibir os dados      
    def EditarDados(self, valor):
        if x == 1:
         try:
          update(variconexao,"UPDATE usuario SET email ='"+valor+"' WHERE id_user ='"+self._return+"';")
          return True
         except sqlite3.Error as e:
          print(e)
        elif x == 2:
         try:
          update(variconexao,"UPDATE usuario SET nome_user ='"+valor+"' WHERE id_user ='"+self._return+"';")
          return True
         except sqlite3.Error as e:
          print(e)
        elif x == 3:
         try:
          update(variconexao,"UPDATE usuario SET telefone ='"+valor+"' WHERE id_user ='"+self._return+"';")
          return True
         except sqlite3.Error as e:
          print(e)
        elif x == 4:
         try:
          update(variconexao,"UPDATE usuario SET data_aniver ='"+valor+"' WHERE id_user ='"+self._return+"';")
          return True
         except sqlite3.Error as e:
          print(e)
        else:
            print("ok")
# metodo para editar os dados do usuario