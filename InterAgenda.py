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
    res = select(variconexao,"SELECT * FROM calendario;")
    print(res)
    
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
btn_cadastrar.pack(side=LEFT)

principal.mainloop()

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



# def consultar():
#   arvore.delete(*arvore.get_children()) #limpar tree view
#   banco() # chamar conexão com o banco
#   cursor.execute("SELECT * FROM `aluno` ORDER BY `nome` ASC") # seleção com ordenamento por nome
#   fetch = cursor.fetchall() # retorna os resultados como tuplas e armazena em fetch
#   for dados in fetch: # insere tuplas do fetch na árvore
#     arvore.insert('', 'end', values=(dados[0],dados[1], dados[2], dados[3]))
#   cursor.close() # encerrar cursor
#   conexao.close() # encerrar conexão
    
# def sair():
#     resultado = tkMessageBox.askquestion('Cadastro Alunos', 'Tem certeza que deseja sair?', icon="warning") #pergunta se deseja realmente sair
#     if resultado == 'yes':
#         principal.destroy() # fecha tela
#         exit()

# def deletar():
#   banco()
#   item = arvore.selection()[0] # recebe item selecionado na árvore
#   resultado = tkinter.messagebox.askquestion("Confirmação", "Tem certeza que deseja excluir aluno?", icon="warning") # pede confirmação do usuário
#   if resultado == 'yes':
#     for item in arvore.selection():
#       cursor.execute("DELETE FROM aluno WHERE id = ?", (arvore.set(item, '#1'),)) #apaga item selecionado do banco
#       arvore.delete(item) #apaga item selecionado da árvore
#   conexao.commit()
#   conexao.close()

# dadosativ = "INSERT INTO `atividade` (nome_atividade,tipo_atividade,local_atividade,comentario) VALUES('"+ativ.get()+"','"+tipoativ.get()+"','"+local.get()+"','"+coment.get()+"')"
#     insert(variconexao,dadosativ)