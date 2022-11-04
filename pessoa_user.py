class Pessoa_User:
    def __init__(self):
        self.CPF = input("Digite seu CPF: ")
        self.__email = input("Digite seu email: ")
        self.__senha = input("Digite sua senha: ")
        self.__telefone = input('Digite seu telefone: ')
        self.__dict = {}
        self.__nm_user = None
        self.__dataniver = None
# atributos usuario
    def ConfirmaDado(self):
        x= input("Confirme o seu CPF: ")
        y= input("Confirme a sua senha: ")
        if self.CPF == x and self.__senha == y:
            print("\033[0;49;32mtudo certo")
            return 's'
        else:
            print("\033[0;49;31merro os dados digitados não coincidem")
            print('\033[1;94m')
            return 'n'
# metodo para confirmar dados
    def AddDados(self):
        x = [
            self.__email, self.__senha, self.__telefone, self.__nm_user, self.__dataniver
        ]
        if self.__dict.get(self.CPF):
            print("\033[0;49;31mJá existe esse usuario", self.CPF)
        else:
            self.__dict[self.CPF] = x
# metodo para adicionar dados ao dicionario
    def Login(self):
        a = input('Digite seu CPF: ')
        b = input("Digite sua senha: ")
        try:
         y = self.__dict[a]
        except:
         print('\033[0;49;31mnão existe usuario ',a)
        if a in self.__dict.keys() and y[1] == b:
            print('\033[0;49;32mtudo certo')
            return a
        else:
            print("\033[0;49;31merro senha incorreta")
            print('\033[1;33m')
            return 'n'
# metodo que autoriza o usuario a entrar no planner
    def AlterarSenha(self,newsenha):
        self.__nm_user = newsenha
        val = input("Digite seu usuario: ")
        try:
         y = self.__dict[val]
        except:
         print('\033[0;49;31mnão existe usuario ',val)
         print('\033[1;33m')
        else:
         y[1] = self.__nm_user
         print("\033[0;49;32mtudo certo")
         print('\033[1;33m')
# metodo para alterar a senha
    def ExibirDados(self, val):
        y=self.__dict[val]
        print("Usuario numero: {}\nNome: {}\nSenha: {}\nEmail: {}\nTelefone: {}\nDataAniversario: {}\nse algum dado estiver none é porque ele ainda não foi definida".format(val,y[3],y[1],y[0],y[2],y[4]))
# metodo para exibir os dados      
    def EditarDados(self, x, val, val2):
        if x == 1:
            self.__nm_user = val
            y = self.__dict[val2]
            y[3] = self.__nm_user
            print("\033[0;49;32mtudo certo")
            return self.__dict
        elif x == 2:
            self.__email = val
            y = self.__dict[val2]
            y[0] = self.__email
            print("\033[0;49;32mtudo certo")
            return self.__dict
        elif x == 3:
            self.__telefone = val
            y = self.__dict[val2]
            y[2] = self.__telefone
            print("\033[0;49;32mtudo certo")
            return self.__dict
        elif x == 4:
            self.__dataniver = val
            y = self.__dict[val2]
            y[4] = self.__dataniver
            print("\033[0;49;32mtudo certo")
            return self.__dict
        else:
            print("ok")
# metodo para editar os dados do usuario