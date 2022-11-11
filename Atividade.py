Atividade = {}
class Atividades:
  def __init__ (self):
    self.__nomeAtividade = None 
    self.__localAtividade = None
    
# metodo para editar a atividade ou cria-la    
  def editarAtividade(self): 
     self.__nomeAtividade = input("Digite o nome da Atividade:")
     if Atividade.get(self.__nomeAtividade):
       print("Ja existe uma atividade com este nome ", self.__nomeAtividade)
     else:
       self.__localAtividade = input("Em que local sua atividade será realizada?")
     Atividade [self.__nomeAtividade] = (self.__localAtividade)
     print("CADASTRO FINALIZADO!")
     edit = input("Você deseja editar o nome  da atividade (s/n)?")
     if edit == 's':
       new = input("Qual atividade você deseja editar?")
       atividade1 = input("Novo nome:")
       if new in Atividade.keys():
         Atividade[new] = atividade1
       print(Atividade)
       return atividade1    
     else:
       edit2 = input("Você deseja mudar o local em que a atividade será realizada (s/n)?")
       if edit2 == 's':
         new2 = input("Qual atividade você deseja editar?")
         local1 = input("Digite o novo local:")
         if new2 in Atividade.keys():
           Atividade[new2] = local1

         print(Atividade)
     return self.__nomeAtividade
# metodo que adiciona comentarios    
  def adicionar_comentario(self):
    vr = input("Qual o nome da sua pasta de recados?")
    file = open(vr,'a+')
    file.write(input('Adicione um comentário a atividade:'))
    file.seek(0,0)
    print(file.read())
# metodo para retornar o local da atividade para a classe calendario    
  def GetLocal(self):
   return self.__localAtividade