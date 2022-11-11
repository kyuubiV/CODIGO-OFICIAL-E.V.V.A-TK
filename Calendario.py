from Atividade import *
from ConexaoBD import *
from Banco import *



class Calendario:
  def __init__(self):
    self.dia = None
    self.mes = None
    self.ano = None
    self.hora = None
    self.atividade = None
  def AgendarAtividade(self):
    if  dia.get() == "" or mes.get() == ""  or ano.get() == ""or hora.get() == ""or ativ.get() == ""or local.get() == "":
    tkinter.messagebox.showinfo(title="Erro",message="Preencha todos os campos!")
  # se não, faz o registro no banco de dados
    else:
    insert(variconexao,"INSERT INTO `calendario`(dia,mes,ano.horario) VALUES")
    cursor.execute("INSERT INTO `aluno` (nome, sobrenome, email) VALUES(?, ?, ?)", (str(nome.get()), str(sobrenome.get()), str(email.get())))
    conexao.commit() # validar inserção
    nome.delete(0,"end") # limpar campo nome
    sobrenome.delete(0,"end") # limpar campo sobrenome
    email.delete(0,"end") # limpar campo e-mail
    cursor.close() # encerrar cursor
    conexao.close() # encerrar conexão
    tkinter.messagebox.showinfo(title="Sucesso!", message="Aluno cadastrado!") # mensagem que inserção ocorreu

import tkinter.messagebox
from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from ConexaoBD import *


cor1 = "#B0C4DE"
cor2 = "#6959CD"
principal = Tk()
principal.title("Agenda")
principal.config(background = cor1)
principal.geometry("500x300")

def cadastrar():
  # se houver campos em branco, exibe mensagem de erro
  if  nome.get() == "" or sobrenome.get() == ""  or email.get() == "":
    tkinter.messagebox.showinfo(title="Erro",message="Preencha todos os campos!")
  # se não, faz o registro no banco de dados
  else:
    banco()# chamar função para conectar ao banco
    cursor.execute("INSERT INTO `aluno` (nome, sobrenome, email) VALUES(?, ?, ?)", (str(nome.get()), str(sobrenome.get()), str(email.get())))
    conexao.commit() # validar inserção
    nome.delete(0,"end") # limpar campo nome
    sobrenome.delete(0,"end") # limpar campo sobrenome
    email.delete(0,"end") # limpar campo e-mail
    cursor.close() # encerrar cursor
    conexao.close() # encerrar conexão
    tkinter.messagebox.showinfo(title="Sucesso!", message="Aluno cadastrado!") # mensagem que inserção ocorreu

def consultar():
  arvore.delete(*arvore.get_children()) #limpar tree view
  banco() # chamar conexão com o banco
  cursor.execute("SELECT * FROM `aluno` ORDER BY `nome` ASC") # seleção com ordenamento por nome
  fetch = cursor.fetchall() # retorna os resultados como tuplas e armazena em fetch
  for dados in fetch: # insere tuplas do fetch na árvore
    arvore.insert('', 'end', values=(dados[0],dados[1], dados[2], dados[3]))
  cursor.close() # encerrar cursor
  conexao.close() # encerrar conexão
    
def sair():
    resultado = tkMessageBox.askquestion('Cadastro Alunos', 'Tem certeza que deseja sair?', icon="warning") #pergunta se deseja realmente sair
    if resultado == 'yes':
        principal.destroy() # fecha tela
        exit()

def deletar():
  banco()
  item = arvore.selection()[0] # recebe item selecionado na árvore
  resultado = tkinter.messagebox.askquestion("Confirmação", "Tem certeza que deseja excluir aluno?", icon="warning") # pede confirmação do usuário
  if resultado == 'yes':
    for item in arvore.selection():
      cursor.execute("DELETE FROM aluno WHERE id = ?", (arvore.set(item, '#1'),)) #apaga item selecionado do banco
      arvore.delete(item) #apaga item selecionado da árvore
  conexao.commit()
  conexao.close()

# variáveis
nome = StringVar()
sobrenome = StringVar()
email = StringVar()



def consultar():
  arvore.delete(*arvore.get_children()) #limpar tree view
  banco() # chamar conexão com o banco
  cursor.execute("SELECT * FROM `aluno` ORDER BY `nome` ASC") # seleção com ordenamento por nome
  fetch = cursor.fetchall() # retorna os resultados como tuplas e armazena em fetch
  for dados in fetch: # insere tuplas do fetch na árvore
    arvore.insert('', 'end', values=(dados[0],dados[1], dados[2], dados[3]))
  cursor.close() # encerrar cursor
  conexao.close() # encerrar conexão
    
def sair():
    resultado = tkMessageBox.askquestion('Cadastro Alunos', 'Tem certeza que deseja sair?', icon="warning") #pergunta se deseja realmente sair
    if resultado == 'yes':
        principal.destroy() # fecha tela
        exit()

def deletar():
  banco()
  item = arvore.selection()[0] # recebe item selecionado na árvore
  resultado = tkinter.messagebox.askquestion("Confirmação", "Tem certeza que deseja excluir aluno?", icon="warning") # pede confirmação do usuário
  if resultado == 'yes':
    for item in arvore.selection():
      cursor.execute("DELETE FROM aluno WHERE id = ?", (arvore.set(item, '#1'),)) #apaga item selecionado do banco
      arvore.delete(item) #apaga item selecionado da árvore
  conexao.commit()
  conexao.close()

# variáveis
dia= StringVar()
mes = StringVar()
ano = StringVar()
hora = StringVar()
ativ = StringVar()
local = StringVar()



# frame
topo = Frame(principal, width=300, height=50, bd=1, relief="raise")
topo.pack(side=TOP)
centro = Frame(principal, width=300, height=400, bd=1, relief="raise", background=cor1)
centro.pack(side=TOP)
Forms = Frame(centro, width=100, height=100, background=cor1)
Forms.pack(side=TOP)
Buttons = Frame(centro, width=100, height=100, background=cor1, relief="raise")
Buttons.pack(side=BOTTOM)

# labels
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
txt_local = Label(Forms, text="Local", font=('arial', 10), bd=15, background=cor1)
txt_local.grid(row=2, stick="e")
txt_result = Label(Buttons, background=cor1)
txt_result.pack(side=TOP)

# entrys
dia = Entry(Forms, textvariable=dia, width=5)
dia.grid(row=0, column=1,sticky = "w")
mes = Entry(Forms, textvariable= mes, width=5)
mes.grid(row=0, column=2,sticky = "w")
ano = Entry(Forms, textvariable= ano, width=8)
ano.grid(row=0, column=4,sticky = "e")
hora = Entry(Forms, textvariable= hora, width=8)
hora.grid(row=0, column=7,sticky = "w")
atividade = Entry(Forms,textvariable = ativ,width=10)
atividade.grid(row=1, column=1)
local = Entry(Forms,textvariable = local,width=10)
local.grid(row=2, column=1)


# botões
btn_cadastrar = Button(Buttons, width=10, text="Cadastrar", command=cadastrar)
btn_cadastrar.pack(side=LEFT)


# btn_consultar = Button(Buttons, width=10, text="Consultar", command=consultar)
# btn_consultar.pack(side=LEFT)
# btn_sair = Button(Buttons, width=10, text="Excluir", command=deletar)
# btn_sair.pack(side=LEFT)
# btn_sair = Button(Buttons, width=10, text="Sair", command=sair)
# btn_sair.pack(side=LEFT)

# treeview
# scrollbary = Scrollbar(direita, orient=VERTICAL)
# scrollbarx = Scrollbar(direita, orient=HORIZONTAL)
# arvore = ttk.Treeview(direita, columns=("Id","Nome", "Sobrenome", "Email"), selectmode="extended", height=200, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
# scrollbary.config(command=arvore.yview)
# scrollbary.pack(side=RIGHT, fill=Y)
# scrollbarx.config(command=arvore.xview)
# scrollbarx.pack(side=BOTTOM, fill=X)
# arvore.heading('Id', text="ID", anchor=W)
# arvore.heading('Nome', text="Nome", anchor=W)
# arvore.heading('Sobrenome', text="Sobrenome", anchor=W)
# arvore.heading('Email', text="E-mail", anchor=W)
# arvore.column('#0', stretch=NO, minwidth=0, width=0)
# arvore.column('#1', stretch=NO, minwidth=0, width=80)
# arvore.column('#2', stretch=NO, minwidth=0, width=80)
# arvore.column('#3', stretch=NO, minwidth=0, width=80)
# arvore.pack()

principal.mainloop()

    try:
      self.dia = input("Insira o dia: ")
      self.mes = input("Insira o mês: ")
      self.ano = input("Insira o ano: ")
      self.hora = input("Insira o horário(00:00): ")
      self.atividade = Atividades()
      
      data = "INSERT INTO calendario (dia,mes,ano,horario) VALUES ('"+self.dia+"','"+self.mes+"','"+self.ano+"','"+self.hora+"'); "
      insert(variconexao,data)
      res = select(variconexao,data)
      print(res)
      
    except sqlite3.Error as e:
     print(e)