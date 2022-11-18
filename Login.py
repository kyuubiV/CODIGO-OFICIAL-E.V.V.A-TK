import tkinter.messagebox
from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from Pessoa import*
from Erro import *
from emailenviator import *
from interface import *
from Menu_Principal import *
import random
def Login():
  retorno=None
  cor1 = "#B0C4DE"
  cor2 = "#6959CD"
  principal = Tk()
  principal.title("Login")
  principal.config(background = cor1)
  principal.geometry("500x300")

  email = StringVar()
  senha = StringVar()
#commands
  def TrocaSenha():
   x = random.randint(1000,9999)
   cod= str(x)
   email1 = askstring('CONFIRMAR EMAIL', "confirme seu email!")
   tel1 = askstring('CONFIRMAR TELEFONE', 'Confirme seu telefone!')
   EmailEnviator(email1,cod)
   confema = askstring('CONFIRMA CODIGO', 'Coloque o codigo que enviamos para o seu email aqui!')
   if confema == cod:
    newsenha = askstring('DIGITAR NOVA SENHA', 'Digite sua nova senha!')
    user=Pessoa(email1,newsenha,tel1)
    ret=user.AlterarSenha()
    if ret == True:
      tkinter.messagebox.showinfo(title="aviso",message='Tudo certo sua senha foi atualizada')
    elif ret == False:
      tkinter.messagebox.showinfo(title="Erro",message='Credenciais invalidas alteração de senha cancelada',icon ="warning")
   else:
    tkinter.messagebox.showinfo(title="Erro",message='valor digitado incorreto!',icon ="warning")

  def entrar():
    principal.withdraw()

    principal.withdraw()
     
  def Pronto():
   if  email.get() == "" or senha.get() == "":
    tkinter.messagebox.showinfo(title="Erro",message="Preencha todos os campos!",icon ="warning")
   user=Pessoa(email.get(),senha.get(),None)
   ret=user.Login()
   if len(ret) == 1:
    tkinter.messagebox.showinfo(title="aviso",message=f'Tudo certo')
    principal(ret)
    email.delete(0,"end") 
    senha.delete(0,"end")
   else:
    tkinter.messagebox.showinfo(title="Erro",message=f'Credenciais invalidas',icon ="warning")

#windows
  topo = Frame(principal, width=300, height=50, bd=1, relief="raise")
  topo.pack(side=TOP)
  centro = Frame(principal,width = 500, height = 300, bd = 1, relief = "raise", background=cor2)
  centro.pack(side=TOP)
  Forms = Frame(centro, width=500, height=300, background=cor2)
  Forms.pack(side=TOP)
  Buttons = Frame(centro, width=500, height=50, background=cor2, relief="raise")
  Buttons.pack(side=LEFT)

#labels
  txt_titulo = Label(topo, width= 23, font=('arial', 18), text = "Login", background=cor2)
  txt_titulo.pack()
  txt_email = Label(Forms,height=4, text="E-mail:", font=('arial', 10), bd=20, background=cor2)
  txt_email.grid(row=0, stick="e")
  txt_senha = Label(Forms,height=4, text="Senha:", font=('arial', 10), bd=20, background=cor2)
  txt_senha.grid(row=1, stick="e")
  txt_result = Label(Buttons, background=cor2)
  txt_result.pack(side=TOP)
#entradas
  email = Entry(Forms, textvariable=email, width=25)
  email.grid(row=0, column=1)
  senha = Entry(Forms, textvariable=senha, width=25,show="*")
  senha.grid(row=1, column=1)
#Buttons
  btn_entrar = Button(Buttons, width=10, text="Entrar", command=Pronto)
  btn_entrar.pack(side=LEFT)
  btn_ntncad = Button(Buttons, width=13, text=" Não tenho cadastro", command=entrar)
  btn_ntncad.pack(side=LEFT)
  btn_esqcms = Button(Buttons, width=10, text="Esqueci a senha", command=TrocaSenha)
  btn_esqcms.pack(side=LEFT)
  principal.mainloop()