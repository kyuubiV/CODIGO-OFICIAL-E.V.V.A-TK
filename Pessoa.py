class Pessoa:
    def __init__(self):
        self.CPF = input("Digite seu CPF: ")
        self._email = input("Digite seu email: ")
        self._senha = input("Digite sua senha: ")
        self._telefone = input('Digite seu telefone: ')
        self._dict = {}   
        self._nm_user = None
        self._dataniver = None
# atributos usuario
    def ConfirmaDado(self):
        x= input("Confirme o seu CPF: ")
        y= input("Confirme a sua senha: ")
        if self.CPF == x and self._senha == y:
            print("\033[0;49;32mTudo certo!")
            return 's'
        else:
            print("\033[0;49;31merro os dados digitados não coincidem")
            print('\033[1;94m')
            return 'n'
# metodo para confirmar dados        
    def AddDados(self):
        x = [self._email, self._senha, self._telefone, self._nm_user, self._dataniver]
        if self._dict.get(self.CPF):
            print("\033[0;49;31mJá existe esse usuario", self.CPF)
        else:
            self._dict[self.CPF] = x