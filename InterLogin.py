import tkinter.messagebox
from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from ConexaoBD import *

Re = select(variconexao,"SELECT senha FROM `usuario` ")
print(Re)

cor1 = "#B0C4DE"
cor2 = "#6959CD"
principal = Tk()
principal.title("Agenda")
principal.config(background = cor1)
principal.geometry("500x300")

email = StringVar()
senha = StringVar()

def logar():
  if  email.get() == "" or senha.get() == "":
    tkinter.messagebox.showinfo(title="Erro",message="Preencha todos os campos!") 
  else:
    email1 = select(variconexao,"SELECT email FROM `usuario` ")
    senha1 = select(variconexao,"SELECT senha FROM `usuario` ")
    if  email.get() == email1:
      if senha.get() == senha1:
        tkinter.messagebox.showinfo(title="",message="Bem-vindo!") 
    else:
      tkinter.messagebox.showinfo(title="Erro",message="Usuário não encontrado.")



# Frame
topo = Frame(principal, width=300, height=50, bd=1, relief="raise")
topo.pack(side=TOP)
centro = Frame(principal, width=300, height=400, bd=1, relief="raise", background=cor1)
centro.pack(side=TOP)
Forms = Frame(centro, width=500, height=300, background=cor1)
Forms.pack(side=TOP)
Buttons = Frame(centro, width=100, height=100, background=cor1, relief="raise")
Buttons.pack(side=BOTTOM)


# Labels
txt_titulo = Label(topo, width=600, font=('arial', 18), text = "Login", background=cor2)
txt_titulo.pack()
txt_dia = Label(Forms, text="E-mail: ", font=('arial', 10), bd=10, background=cor1)
txt_dia.grid(row=1, sticky="e")
txt_mes = Label(Forms, text="Senha: ", font=('arial', 10), bd=10, background=cor1)
txt_mes.grid(row=2, column=0,sticky = "e")
txt_es = Label(Forms, text=" ", font=('arial', 10), bd=10, background=cor1)
txt_es.grid(row=0, column=3,sticky = "e")
txt_esp = Label(Buttons, text=" ", font=('arial', 10), bd=10, background=cor1)
txt_esp.pack(side=BOTTOM)

# Entrys
email = Entry(Forms, textvariable=email, width=20)
email.grid(row=1, column=1,sticky = "e")
senha= Entry(Forms, textvariable= senha, width=15)
senha.grid(row=2, column=1,sticky = "w")

btn_conf = Button(Buttons,width=10,text="Confirmar",command = logar)
btn_conf.pack(side=BOTTOM)






principal.mainloop()



