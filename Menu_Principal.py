import tkinter.messagebox
from Calendario import *
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import calendar
from User import *
from tkinter.simpledialog import askstring
from InterAgenda import *
from InterCalen import *

def mn_principal(usuario):
  def agenda():
    windowsmp.withdraw()
    Agenda()
  def calendario():
   windowsmp.withdraw()
   Calendario()
  windowsmp = Tk()
  windowsmp.geometry("600x350")

#amarelo, vermelho e azul, roxo e vermelho rxo clarinho 
  corum = "#FFFF00"
  corois = "#FF0000"
  cores = "#00BFFF"
  corb = "#7B68EE"
  corr = "#FF0000"
  coroxo = "#6A5ACD"
#edt txt
  windowsmp.title("Menu principal")
  windowsmp.config(background =cores)
#testando o frame 
  topo = Frame(windowsmp, width=600, height=100, bd=1, relief="raise")
  topo.pack(side=TOP)
  esquerda = Frame(windowsmp, width=500, height=350, background=cores)
  esquerda.pack(side=LEFT)
  direita = Frame(windowsmp, width=200, height=350, bd=1, relief="raise", background = corr)
  direita.pack(side=RIGHT)

# labels

  txt_om = Label(topo, width=600, font=('serif', 17), text = "Seja Bem Vindo ao Little Calendar.", background="#836FFF")
  txt_om.pack()


  Forms = Frame(esquerda, width=500, height=175, background=coroxo)
  Forms.pack(side=LEFT) 


  Formsoutrolado = Frame(direita, width= 300, height=175,  background=corr)
  Formsoutrolado.pack(side=RIGHT)

  # img = PhotoImage(file="logo_trab.png")
  # #figura1 = Label(Forms,image=img)
  # figura1 = Label(Forms, image=img,width=100,bd=20,background=coroxo)
  # figura1.grid(row=2,column=8)

  txtus= Label(Formsoutrolado,width=16, font=('arial', 10), text = 'Usuário', bd=10,background = corr)
  txtus.grid(row=1, column=1)

  #atv = Label(Forms, text="A\nT\nI\nV\nI\nD\nA\nD\nE\n ", font=#('arial', 6), bd=10, background=corum )

  #atv.grid(row= 0, column=4 )

  # Buttons = Frame(esquerda, width=20, height=20, background= cores, relief="raise")
  # Buttons.pack(side=TOP)

#commands
  def visu_dads():
   x=usuario[0]
   user= User("","","")
   res = user.ExibirDados(x[0])
   for dados in res:
    tkinter.messagebox.showinfo(title ='Dados',message = f'email: {dados[1]}\nSenha: {dados[2]} \nNome de usuario: {dados[3]}\nTelefone:  {dados[4]}\nData de aniversario: {dados[5]}') 
  def sair():
    
    resultado = tkMessageBox.askquestion('Cadastro Usuários', 'Tem certeza que deseja sair?', icon="warning") 
    if resultado == 'yes':
        windowsmp.destroy() 
        exit()
      
  def atlz_usu():
    x=usuario[0]
    user= User("","","")
    attdads = askstring('DIGITE O NOVO DADO', '1.Nome de usuario\n2.Telefone\n3.Data de aniversario')
    if attdads == '1'or attdads == '2'or attdads == '3':
      newdads = askstring('ATUALIZA DADO','Digite o valor')
      res = user.EditarDados(newdads,str(x[0]),attdads)
      if res == True:
         tkinter.messagebox.showinfo(title="aviso",message=f'Tudo certo')
      else:
         print(res)
         tkinter.messagebox.showinfo(title="aviso",message=f'Algo deu errado',icon ="warning")
    else:
      tkinter.messagebox.showinfo(title="aviso",message=f'Digite o valor foi pedido',icon ="warning")
#buttons

  buttonVD = Button(Formsoutrolado,width=15, text = "Ver Perfl", font=('arial',10), bd=8,background= cores, command = visu_dads)
  buttonVD.grid(row=2, column=1)

  buttonED = Button(Formsoutrolado,width=15, text = "Atualizar perfil", font=('arial',10), bd=8,background= cores, command = atlz_usu)
  buttonED.grid(row=3, column=1)

  atv= Label(Forms,width=15, font=('arial', 12), text = 'ATIVIDADES:', bd=10,background = coroxo)
  atv.grid(row=0, column=1)

  buttons_aa = Button(Forms,width = 12, text="Agendar Atividade", font=('arial', 8), bd=10, background=corb, command = agenda)
  buttons_aa.grid(column=1,row=1)

  button_ba =Button(Forms, width=12, text="Buscar atividade", font=('arial', 8), bd=10, background=corb)
  button_ba.grid(column=1,row=2)

  button_va = Button(Forms,width=12,text="Visualizar Atividade", font=('arial', 8), bd=10, background=corb,command=calendario)
  button_va.grid(column=1,row=3)

  buttons = Button(Forms, width=12, text= 'SAIR', font= ('arial', 8),bd=10, background= corb,command= sair)
  buttons.grid(column=1,row=4)

  windowsmp.mainloop()
#imagem

#label_imagem = Label(root, image=img).pack()

# txt_result = Label(Buttons, background=corum)
# txt_result.pack(side=TOP)
#bt editar dados do usuario, sair, 
"""
#texto dentro da jan
txt_om = Label(windowsmp, text="Seja Bem Vindo ao Little Calendar", background = cores)
txt_om.grid(column=2, row=3)

botaumaa = Button(windowsmp, text="Agendar atividade", command=Calendario)
botaumaa.grid(column= 2, row=2)
#buscar
botaumba = Button(windowsmp, text="Buscar Atividade", command=Calendario)
botaumba.grid(column= 2, row=3)
#visualizar calendario 
botaumvs = Button(windowsmp, text="Visualizar Calendário", command=vcalendario)
botaumvs.grid(column= 2, row=4)
#Editar dados
#Sair 
"""