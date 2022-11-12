import tkinter.messagebox
from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from Pessoa import*
cor1 = "#B0C4DE"
cor2 = "#6959CD"
principal = Tk()
principal.title("Cadastro de usuários")
principal.config(background = cor1)
principal.geometry("500x300")

email = StringVar()
senha = StringVar()
telefone = StringVar()

def sair():
    resultado = tkMessageBox.askquestion('Cadastro Usuários', 'Tem certeza que deseja sair?', icon="warning") 
    if resultado == 'yes':
        principal.destroy() 
        exit()

def Pronto():
  if  email.get() == "" or senha.get() == ""  or telefone.get() == "":
    tkinter.messagebox.showinfo(title="Erro",message="Preencha todos os campos!",icon ="warning")
  else:
    email1 = askstring('Email', "confirme seu email!")
    senha1 = askstring('Senha', 'Confirme sua senha!',show="*")
    if email.get() != email1 or senha.get() != senha1:
     showinfo('ERRO', 'Erro dados não coincidem',icon ="warning")
    else:
     showinfo('AVISO', 'tudo certo')
     usuario = Pessoa(email,senha, telefone)
     usuario.AddDados()
     email.delete(0,"end") 
     senha.delete(0,"end")
     telefone.delete(0,"end")
      
#windows
topo = Frame(principal, width=300, height=50, bd=1, relief="raise")
topo.pack(side=TOP)
centro = Frame(principal,width = 400, height = 450, bd = 1, relief = "raise", background=cor2)
centro.pack(side=TOP)
Forms = Frame(centro, width=500, height=350, background=cor2)
Forms.pack(side=TOP)
Buttons = Frame(centro, width=50, height=50, background=cor2, relief="raise")
Buttons.pack(side=LEFT)
#labels
txt_titulo = Label(topo, width= 25, font=('arial', 18), text = "Cadastro de Usuários", background=cor2)
txt_titulo.pack()
txt_email = Label(Forms, text="E-mail:", font=('arial', 10), bd=20, background=cor2)
txt_email.grid(row=0, stick="e")
txt_senha = Label(Forms, text="Senha:", font=('arial', 10), bd=20, background=cor2)
txt_senha.grid(row=1, stick="e")
txt_telefone = Label(Forms, text="Telefone:", font=('arial', 10), bd=20, background=cor2)
txt_telefone.grid(row=2, stick="e")

txt_result = Label(Buttons, background=cor1)
txt_result.pack(side=TOP)
#entradas
email = Entry(Forms, textvariable=email, width=25)
email.grid(row=0, column=1)
senha = Entry(Forms, textvariable=senha, width=25,show="*")
senha.grid(row=1, column=1)
telefone = Entry(Forms, textvariable=telefone, width=25)
telefone.grid(row=2, column=1)
#botoes
btn_pronto = Button(Buttons, width=12, text="pronto", command=Pronto)
btn_pronto.pack(side=LEFT)
btn_jtncad = Button(Buttons, width=13, text=" já tenho cadastro", command=None)
btn_jtncad.pack(side=LEFT)
btn_sair = Button(Buttons, width=12, text="Sair", command=sair)
btn_sair.pack(side=LEFT)

