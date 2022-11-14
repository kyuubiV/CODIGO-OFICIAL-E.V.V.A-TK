import tkinter.messagebox
from Calendario import *
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import calendar



def vcalendario():
  y = int(input("Digite o ano desejado:"))
  m = int(input("Digite a data desejada "))
  print(calendar.month(y, m))
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

img = PhotoImage(file="evvaslog.png")
#figura1 = Label(Forms,image=img)
figura1 = Label(Forms, image=img,width=100,bd=20,background=coroxo)
figura1.grid(row=2,column=7)

txtus= Label(Formsoutrolado,width=16, font=('arial', 10), text = 'Usuário', bd=10,background = corr)
txtus.grid(row=1, column=1)

#atv = Label(Forms, text="A\nT\nI\nV\nI\nD\nA\nD\nE\n ", font=#('arial', 6), bd=10, background=corum )

#atv.grid(row= 0, column=4 )

# Buttons = Frame(esquerda, width=20, height=20, background= cores, relief="raise")
# Buttons.pack(side=TOP)
#bottons
def Profile():
  tkinter.messagebox.showinfo(title="Your Profile",message="USUARIO VAI ETSAR AQUI OH")
  #background="#87CEFA" messagebox color
buttonVD = Button(Formsoutrolado,width=15, text = "Visualizar Dados", font=('arial',10), bd=8,background= cores, command = Profile)
buttonVD.grid(row=2, column=1)
#tryforimage

#delimitytryforimage
buttonED = Button(Formsoutrolado,width=15, text = "Editar Dados", font=('arial',10), bd=8,background= cores)
buttonED.grid(row=3, column=1)

atv= Label(Forms,width=15, font=('arial', 15), text = 'ATIVIDADES:', bd=10,background = coroxo)
atv.grid(row=0, column=1)
buttons_aa = Button(Forms,width = 12, text="Agendar Atividade", font=('arial', 8), bd=10, background=corb, command = Calendario)
buttons_aa.grid(column=1,row=1)

button_ba =Button(Forms, width=12, text="Buscar atividade", font=('arial', 8), bd=10, background=corb)
button_ba.grid(column=1,row=2)

button_va = Button(Forms,width=12,text="Visualizar Atividade", font=('arial', 8), bd=10, background=corb)

button_va.grid(column=1,row=3)
buttons = Button(Forms, width=12, text= 'SAIR', font= ('arial', 8),bd=10, background= corb)
buttons.grid(column=1,row=4)
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
windowsmp.mainloop()