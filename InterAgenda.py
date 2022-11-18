import tkinter.messagebox
from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from ConexaoBD import *
import calendar
from datetime import *

# Criação tela principal
cor1 = "#B0C4DE"
cor2 = "#6959CD"
principal = Tk()
principal.title("Agenda")
principal.config(background = cor1)
principal.geometry("500x300")

# Variáveis da interface
dia= StringVar()
mes = StringVar()
ano = StringVar()
hora = StringVar()
ativ = StringVar()
tipoativ = StringVar()
local = StringVar()
coment = StringVar()

# Agendar data e Atividade no Calendário.
def Agendar():
  
  # Não permetir campos vazios.
  if  dia.get() == "" or mes.get() == ""  or ano.get() == "" or hora.get() == "" or ativ.get() == "" or tipoativ.get() == "" or local.get() == "":   tkinter.messagebox.showinfo(title="Erro",message="Preencha todos os campos!") 
    
  # Não perfitir datas inconsistentes 
  d = int(dia.get())
  m = int(mes.get())
  a = int(ano.get())
  data_atual = date.today()
  if d < data_atual.day or m < data_atual.month or a < data_atual.year:
    tkinter.messagebox.showinfo(title="Erro",message="Data selecionada está no passado!")
    
  else:
    # Adicionar dados na tabela caléndario.
    dadosdata = "INSERT INTO `calendario` (dia,mes,ano,horario,nome_atividade,tipo_atividade,local_atividade,comentario) VALUES('"+dia.get()+"','"+mes.get()+"','"+ano.get()+"','"+hora.get()+"','"+ativ.get()+"','"+tipoativ.get()+"','"+local.get()+"','"+coment.get()+"')"
    insert(variconexao,dadosdata)
    mes.delete(0,"end") 
    dia.delete(0,"end") 
    ano.delete(0,"end") 
    hora.delete(0,"end")
    ativ.delete(0,"end")
    tipoativ.delete(0,"end")
    local.delete(0,"end")
    coment.delete(0,"end")
    tkinter.messagebox.showinfo(title="Sucesso!", message="Atividade Adicionada") # Mensagem de sucesso
  

    # Verificar dados adicionados pelo terminal(Apens para testar funcionamento)
    # res = select(variconexao,"SELECT * FROM calendario;")
    # print(res)
    
# Frame
topo = Frame(principal, width=300, height=50, bd=1, relief="raise")
topo.pack(side=TOP)
centro = Frame(principal, width=300, height=400, bd=1, relief="raise", background=cor1)
centro.pack(side=TOP)
Forms = Frame(centro, width=500, height=300, background=cor1)
Forms.pack(side=TOP)
comentario = Frame(centro,width = 200,height = 100,bd=1,background = cor1)
comentario.place(x=250,y=50)
Buttons = Frame(centro, width=100, height=100, background=cor1, relief="raise")
Buttons.pack(side=BOTTOM)

# Labels
txt_titulo = Label(topo, width=600, font=('arial', 18), text = "Agendar Atividade", background=cor2)
txt_titulo.pack()
txt_dia = Label(Forms, text="Dia", font=('arial', 10), bd=10, background=cor1)
txt_dia.grid(row=0, sticky="e")
txt_mes = Label(Forms, text="Mês", font=('arial', 10), bd=10, background=cor1)
txt_mes.grid(row=0, column=1,sticky = "e")
txt_ano = Label(Forms, text="Ano", font=('arial', 10), bd=10, background=cor1)
txt_ano.grid(row=0, column=3,sticky = "e")
txt_hora = Label(Forms, text="Horário", font=('arial', 10), bd=10, background=cor1)
txt_hora.grid(row=0, column=6,sticky = "w")
txt_ativ = Label(Forms, text="Atividade", font=('arial', 10), bd=15, background=cor1)
txt_ativ.grid(row=1, stick="e")
txt_tipoativ = Label(Forms, text="Tipo Atividade", font=('arial', 10), bd=15, background=cor1)
txt_tipoativ.grid(row=2, stick="e")
txt_local = Label(Forms, text="Local", font=('arial', 10), bd=15, background=cor1)
txt_local.grid(row=3, stick="e")
txt_coment = Label(comentario,text="Comentário:",font=('arial', 10), bd=15, background=cor1)
txt_coment.grid(row=0,stick = "w")
txt_result = Label(Buttons, background=cor1)
txt_result.pack(side=TOP)

# Entrys
dia = Entry(Forms, textvariable=dia, width=5)
dia.grid(row=0, column=1,sticky = "w")
mes = Entry(Forms, textvariable= mes, width=5)
mes.grid(row=0, column=2,sticky = "w")
ano = Entry(Forms, textvariable= ano, width=8)
ano.grid(row=0, column=4,sticky = "e")
hora = Entry(Forms, textvariable= hora, width=8)
hora.grid(row=0, column=7,sticky = "w")
ativ = Entry(Forms,textvariable = ativ,width=10)
ativ.grid(row=1, column=1)
tipoativ = Entry(Forms,textvariable = tipoativ,width=10)
tipoativ.grid(row=2, column=1)
local = Entry(Forms,textvariable = local,width=10)
local.grid(row=3, column=1)
coment=Entry(comentario,textvariable=coment,width=20)
coment.grid(row=1)

# Botões
btn_cadastrar = Button(Buttons, width=10, text="Cadastrar", command=Agendar)
btn_cadastrar.pack(side=RIGHT)

btn_voltar = Button(Buttons, width=10, text="Voltar")
btn_voltar.pack(side=LEFT)

principal.mainloop()
