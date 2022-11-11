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
windowsmp.geometry("500x250")
#amarelo, vermelho e azul
corum = "#FFFF00"
corois = "#FF0000"
cores = "#00BFFF"
corb = "#7B68EE"
corr = "#FF0000"
#edt txt
windowsmp.title("Menu principal")
windowsmp.config(background = cores)
#testando o frame 
topo = Frame(windowsmp, width=600, height=50, bd=1, relief="raise")
topo.pack(side=TOP)
esquerda = Frame(windowsmp, width=300, height=300, bd=1, relief="raise", background=corum)
esquerda.pack(side=LEFT)
direita = Frame(windowsmp, width=300, height=300, bd=1, relief="raise")
direita.pack(side=RIGHT)
# labels
txt_om = Label(topo, width=600, font=('arial', 17), text = "Seja Bem Vindo ao Little Calendar", background=corois)
txt_om.pack()
Forms = Frame(esquerda, width=200, height=200, background=cores)
Forms.pack(side=TOP)
Buttons = Frame(esquerda, width=50, height=50, background=corum, relief="raise")
Buttons.pack(side=BOTTOM)
#bottons
buttons_aa = Button(Forms,width = 12, text="Agendar Atividade", font=('arial', 10), bd=15, background=corb, command = Calendario)
buttons_aa.grid(row=0)

button_ba =Button(Forms, width=12, text="Buscar atividade", font=('arial', 10), bd=15, background=corb)
button_ba.grid(row=1)

button_va = Button(Forms,width=12,text="Visualizar Atividade", font=('arial', 10), bd=15, background=corb, command = vcalendario)

button_va.grid(row=2)

txt_result = Label(Buttons, background=corum)
txt_result.pack(side=TOP)
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