from Pessoa import *

class User(Pessoa):
  
    def __init__(self):
        super().__init__()
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
# metodo que autoriza o usuario a entrar no planner
    def AlterarSenha(self,newsenha):
        self._nm_user = newsenha
        val = input("Digite seu usuario: ")
        try:
         y = self._dict[val]
        except:
         print('\033[0;49;31mnão existe usuario ',val)
         print('\033[1;33m')
        else:
         y[1] = self._nm_user
         print("\033[0;49;32mtudo certo")
         print('\033[1;33m')
# metodo para alterar a senha
    def ExibirDados(self, val):
        y=self._dict[val]
        print("Usuario numero: {}\nNome: {}\nSenha: {}\nEmail: {}\nTelefone: {}\nDataAniversario: {}\nse algum dado estiver none é porque ele ainda não foi definida".format(val,y[3],y[1],y[0],y[2],y[4]))
# metodo para exibir os dados      
    def EditarDados(self, x, val, val2):
        if x == 1:
            self._nm_user = val
            y = self._dict[val2]
            y[3] = self._nm_user
            print("\033[0;49;32mtudo certo")
            return self._dict
        elif x == 2:
            self._email = val
            y = self._dict[val2]
            y[0] = self._email
            print("\033[0;49;32mtudo certo")
            return self._dict
        elif x == 3:
            self._telefone = val
            y = self._dict[val2]
            y[2] = self._telefone
            print("\033[0;49;32mtudo certo")
            return self._dict
        elif x == 4:
            self._dataniver = val
            y = self._dict[val2]
            y[4] = self._dataniver
            print("\033[0;49;32mtudo certo")
            return self._dict
        else:
            print("ok")
# metodo para editar os dados do usuario