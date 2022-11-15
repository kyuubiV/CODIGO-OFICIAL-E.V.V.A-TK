import tkinter.messagebox
from Calendario import *
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import calendar
from User import *
def vcalendario():
  y = int(input("Digite o ano desejado:"))
  m = int(input("Digite a data desejada "))
  print(calendar.month(y, m))
windowsmp = Tk()
windowsmp.geometry("500x250")
#amarelo, vermelho e azul, roxo e vermelho k
corum = "#FFFF00"
corois = "#FF0000"
cores = "#00BFFF"
corb = "#7B68EE"
corr = "#FF0000"
#edt txt
windowsmp.title("Menu principal")
windowsmp.config(background = cores)
#comandos
def visu_dads():
  user= User(None,None,None)
  res = user.ExibirDados()
  for dados in res:
   tkinter.messagebox.showinfo(title ='Dados',message = f'email: {dados[1]} \nSenha: {dados[2]} \nNome de usuario: {dados[3]}\nTelefone:  {dados[4]}\nData de aniversario: {dados[5]}') 
def sair():
    resultado = tkMessageBox.askquestion('Cadastro Usuários', 'Tem certeza que deseja sair?', icon="warning") 
    if resultado == 'yes':
        windowsmp.destroy() 
        exit()
#testando o frame 
topo = Frame(windowsmp, width=600, height=50, bd=1, relief="raise")
topo.pack(side=TOP)
esquerda = Frame(windowsmp, width=300, height=500, bd=1, relief="raise", background=cores)
esquerda.pack(side=LEFT)
direita = Frame(windowsmp, width=300, height=500, bd=1, relief="raise", background = corr)
direita.pack(side=RIGHT)

# labels
txt_om = Label(topo, width=600, font=('arial', 17), text = "Seja Bem Vindo ao Little Calendar", background=corois)
txt_om.pack()
Forms = Frame(esquerda, width=600, height=400, background=cores)
Forms.pack(side=TOP) 
Formsoutrolado = Frame(direita, width= 600, height=400,  background=corr)
Formsoutrolado.pack(side=RIGHT)
txtus= Label(Formsoutrolado,width=16, font=('arial', 10), text = 'Usuário', bd=10,background = corr)
txtus.grid(row=0, column=1)

#atv = Label(Forms, text="A\nT\nI\nV\nI\nD\nA\nD\nE\n ", font=#('arial', 6), bd=10, background=corum )

#atv.grid(row= 0, column=4 )

# Buttons = Frame(esquerda, width=20, height=20, background= cores, relief="raise")
# Buttons.pack(side=TOP)

#bottons
buttonED = Button(Formsoutrolado,width=15, text = "Visualizar Dados", font=('arial',10), bd=8,background= cores,command= visu_dads)
buttonED.grid(row=2, column=1)
buttons_aa = Button(Forms,width = 11, text="Agendar Atividade", font=('arial', 6), bd=10, background=corb, command = Calendario)
buttons_aa.grid(column=2,row=0)

button_ba =Button(Forms, width=11, text="Buscar atividade", font=('arial', 6), bd=10, background=corb)
button_ba.grid(column=2,row=1)

button_va = Button(Forms,width=11,text="Visualizar Atividade", font=('arial', 6), bd=10, background=corb)

button_va.grid(column=2,row=2)
buttons = Button(Forms, width=11, text= 'SAIR', font= ('arial', 6),bd=10, background= corb,command = sair)
buttons.grid(column=2,row=3)
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
windowsmp.mainloop()