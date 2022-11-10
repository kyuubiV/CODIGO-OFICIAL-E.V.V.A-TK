import tkinter.messagebox
from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

cor1 = "#B0C4DE"
cor2 = "#6959CD"
principal = Tk()
principal.title("Cadastro de usuários")
principal.config(background = cor1)
principal.geometry("800x450")

email = StringVar()
senha = StringVar()
telefone = StringVar()

topo = Frame(principal, width=500, height=50, bd=1, relief="raise")
topo.pack(side=TOP)
centro = Frame(principal,width = 400, height = 450, bd = 1, relief = "raise", background=cor2)
centro.pack(side=TOP)
Forms = Frame(centro, width=500, height=350, background=cor2)
Forms.pack(side=TOP)
Buttons = Frame(centro, width=50, height=50, background=cor1, relief="raise")
Buttons.pack(side=LEFT)

txt_titulo = Label(topo, width= 33, font=('arial', 18), text = "Cadastro de Usuários", background=cor2)
txt_titulo.pack()
txt_email = Label(Forms, text="E-mail:", font=('arial', 10), bd=20, background=cor2)
txt_email.grid(row=0, stick="e")
txt_senha = Label(Forms, text="Senha:", font=('arial', 10), bd=20, background=cor2)
txt_senha.grid(row=1, stick="e")
txt_telefone = Label(Forms, text="Telefone:", font=('arial', 10), bd=20, background=cor2)
txt_telefone.grid(row=2, stick="e")

txt_result = Label(Buttons, background=cor1)
txt_result.pack(side=TOP)

email = Entry(Forms, textvariable=email, width=25)
email.grid(row=0, column=1)
senha = Entry(Forms, textvariable=senha, width=25)
senha.grid(row=1, column=1)
telefone = Entry(Forms, textvariable=telefone, width=25)
telefone.grid(row=2, column=1)

btn_pronto = Button(Buttons, width=17, text="pronto", command=None)
btn_pronto.pack(side=LEFT)
btn_jtncad = Button(Buttons, width=18, text=" já tenho cadastro", command=None)
btn_jtncad.pack(side=LEFT)
btn_sair = Button(Buttons, width=17, text="Sair", command=None)
btn_sair.pack(side=LEFT)