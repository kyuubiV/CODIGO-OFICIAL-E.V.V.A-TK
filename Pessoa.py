class Pessoa:
    def __init__(self,email,senha,telefone):
        self._email = email
        self._senha = senha
        self._telefone = telefone
        self._dict = {}   
        self._nm_user = None
        self._dataniver = None
# atributos usuario
    def ConfirmaDado(self):
        x= input("Confirme o seu email: ")
        y= input("Confirme a sua senha: ")
        if self._email == x and self._senha == y:
            print("\033[0;49;32mtudo certo")
            return 's'
        else:
            print("\033[0;49;31merro os dados digitados não coincidem")
            print('\033[1;94m')
            return 'n'
# metodo para confirmar dados        
    def AddDados(self):
        x = [self._senha, self._telefone, self._nm_user, self._dataniver]
        if self._dict.get(self._email):
            print("\033[0;49;31mJá existe esse usuario", self._email)
        else:
            self._dict[self._email] = x