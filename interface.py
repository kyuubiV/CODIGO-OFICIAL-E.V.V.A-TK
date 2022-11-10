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


centro = Frame(principal,width = 400, height = 450, bd = 1, relief = "raise", background=cor2)
centro.pack(side=TOP)
Forms = Frame(centro, width=400, height=450, background=cor2)
Forms.pack(side=TOP)
Buttons = Frame(centro, width=100, height=100, background=cor1, relief="raise")
Buttons.pack(side=LEFT)
