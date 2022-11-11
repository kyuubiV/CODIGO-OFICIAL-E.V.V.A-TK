from InterfaceAtividade import *

# from ConexaoBD import *
# from Calendario import *
# from  User import *
# from fun_auxi import *
# from Pessoa import *


# count=0
# inic = input("Vamos inciar?(s/n) ")
# load()
# txt("CADASTRO", 1)
# if inic == 's':
#     user = User()
# # instanciando o usuario
#     load()
#     txt("CONFIRME O CADASTRO", 4)
#     ret = user.ConfirmaDado()
#     while ret == "n":
#       ret = user.ConfirmaDado()
# # confirmando os dados
#     load()
#     user.AddDados()
# # adicionando dados do usuario ao dicionario
#     txt("LOGIN", 5)
#     ret1 = user.Login()
#     while ret1 == "n":
#           ret1 = user.Login()
#           if ret1=="n":
#            count=count+1
#            if count == 3:
#              i = input("Deseja alterar sua senha(s/n) ")
#              if i == 's':
#                nwsen =input("Digite sua nova senha: ") 
#                user.AlterarSenha(nwsen)
#                count = 0
#              else:
#                count = 0
#                pass
#     load()
# # login autorizando o usuario a entrar no planner
# # tela inicial do planner
#     txt("LITTLE CALENDAR",4)
#     print("Olá seja bem vindo")
#     num = int(input("\033[1;34mO que deseja fazer hoje? \n1.Agendar Atividade\n2.Buscar Atividades\n3.visualizar calendario\n4.Editar Dados\n5.Exibir dados\n6.Sair\nDigite o numero desejado: "))
#     while num == 1 or num == 2 or num == 3 or num == 4 or num == 5 or num == 6 or num == 7 or num == 8:
#         if num == 1:
#             load()
#             print('\033[1;94m')
#             usu = Calendario()
#             usu.AgendarAtividade()
#             load()
#         elif num == 2: 
#             load()
#             print('\033[1;94m')
#             usu = Calendario()
#             usu.BuscarAtividade()
            
#         elif num == 3:
#             load()
#             print('\033[1;94m')
#             usu.exibircalendario()
#         elif num == 4:
#             load()
#             print('\033[1;94m')
#             Res=int(input("Oque deseja fazer:\n1.atualizar seu nome de usuario\n2.Atualizar email\n3.atualizar telefone\n4.adicionar sua data de nascimento\n5.não modificar\nR: "))
#             if Res != 5:
#              b=input("Digite o dado escolhido: ")
#              user.EditarDados(Res,b,ret1) 
#             load()
#             print('\033[1;94m')
#         elif num == 5:
#             load()
#             print('\033[1;94m')
#             user.ExibirDados(ret1)
#         else:
#             print("\033[1;31mDeslogando")
#             load()
#             print('\033[1;94m')
#             break
#         txt("LITTLE CALENDAR",4)
#         num = int(input("\033[1;34mO que deseja fazer hoje? \n1.Agendar Atividade\n2.Buscar Atividades\n3.visualizar calendario\n4.Editar Dados\n5.Exibir dados\n6.Sair\nDigite o numero desejado: "))

# else:
#   print("ok:(")