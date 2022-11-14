from tkinter import*
import sqlite3

cor1 = "#0D82FD"
cor2 = "#FF1616"
cor3 = "#FFD230"

#criando login
login = Tk()
login.title("interfce de login")
login.geometry("500x300")
login.configure(background=cor1)
login.resizable(width=FALSE, heigth=FALSE)

#dividindo login
frame_cima = Frame(login, width=310, heinght=50, bg=cor1, relief='flat')
frame_cima.grid(row=0, colunm=0, pady=1, padx=0, sticky=NSEW)
frame_baixo = Frame(login, width=310, heinght=250, bg=cor1, relief='flat')
frame_baixo.grid(row=1, colunm=0, pady=1, padx=0, sticky=NSEW)

login.mainloop()


