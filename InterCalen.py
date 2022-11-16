import tkinter.messagebox
from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from ConexaoBD import *
import calendar 
from datetime import *


# def detalhar():
#   for item in arvore.selection():
#    ativ=select(variconexao,"SELECT * FROM atividade")
#    for item in ativ:
#      print(*item[1])
#      atividade = select(variconexao,"SELECT * FROM atividade WHERE id_calen = '"+item[1]+"'")
#      Ativid
      
#    tkinter.messagebox.showinfo(title="Detalhes",message=atividade) 
#   print(ativ)

def calen():
  # Aparição do calendário referente na tela
  data_atual = date.today()
  ano = data_atual.year
  mese = int(sele.get())
  te =calendar.month(ano,mese)
  cal_year = Label(esquerda, text = te ,font = "Consolas 10 bold")
  cal_year.pack(side=TOP)
  

# Organização do eventos
  scrollbary = Scrollbar(direita, orient=VERTICAL)
  scrollbarx = Scrollbar(direita, orient=HORIZONTAL)
  global arvore  
  arvore = ttk.Treeview(direita, columns=("c1","c2", "c3", "c4","c5","c6","c7","c8"), selectmode="browse", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
  scrollbary.config(command=arvore.yview)
  scrollbary.pack(side=RIGHT, fill=Y)
  scrollbarx.config(command=arvore.xview)
  scrollbarx.pack(side=BOTTOM,fill=X)
  arvore.heading('c1', text="Dia", anchor=W)
  arvore.heading('c2', text="Mês", anchor=W)
  arvore.heading('c3', text="Ano", anchor=W)
  arvore.heading('c4', text="Hora", anchor=W)
  arvore.heading('c5', text="Atividade", anchor=W)
  arvore.heading('c6', text="Tipo", anchor=W)
  arvore.heading('c7', text="Local", anchor=W)
  arvore.heading('c8', text="Comentário", anchor=W)
  arvore.column('#0', stretch=NO, minwidth=0, width=0)
  arvore.column('#1', stretch=NO, minwidth=0, width=30)
  arvore.column('#2', stretch=NO, minwidth=0, width=35)
  arvore.column('#3', stretch=NO, minwidth=0, width=40)
  arvore.column('#4', stretch=NO, minwidth=0, width=50)
  arvore.column('#5', stretch=NO, minwidth=0, width=70)
  arvore.column('#6', stretch=NO, minwidth=0, width=40)
  arvore.column('#7', stretch=NO, minwidth=0, width=40)
  arvore.column('#8', stretch=NO, minwidth=0, width=90)
  arvore.pack(side=TOP)
  # # arvore.delete(*arvore.get_children()) #limpar tree view
  data = select(variconexao,"SELECT * FROM `calendario` WHERE `mes` = '"+sele.get()+"'ORDER BY `dia` ASC")
  id = str(select(variconexao,"SELECT id_calen FROM `calendario` WHERE `mes` = '"+sele.get()+"'"))
  atividade = select(variconexao,"SELECT * FROM `atividade` WHERE `id_calen` = '"+id+"'")
  print(atividade)
  for dados in data: # insere tuplas do fetch na árvore
    for x in atividade:
     arvore.insert('', 'end', values=(dados[2],dados[3], dados[4], dados[5],x[2],x[3],x[4],x[5]))
  arvore.pack(side = RIGHT) 
  
 
  # arvore.pack()
  # direita.destroy()
  

cor1 = "#B0C4DE"
cor2 = "#6959CD"
principal = Tk()
principal.title("Calendário")
principal.config(background = cor1)
principal.geometry("600x300")

selecionar = IntVar()

topo = Frame(principal, width=600, height=50,bd=1, relief="raise",background = cor1)
topo.pack(side=TOP)
direita = Frame(principal,width =300,height = 250,bd=3,relief="raise",background=cor2)
direita.pack(side=RIGHT)
esquerda = Frame(principal,width = 50,heigh = 50,relief = "raise", bd=5)
esquerda.place(x=15,y=90)

txt_selecionar = Label(topo, text="Selecione o mês:", font=('arial', 10), bd=10, background=cor1)
txt_selecionar.grid(row=0, sticky="e")

sele = Entry(topo, textvariable = selecionar, width=5,bd = 3)
sele.grid(row=0, column=1,sticky = "w")


btn_visu = Button(topo, width=5, text="OK", command=calen)
btn_visu.grid(row=1,column=0,stick = "e")
# btn_visu = Button(topo, width=5, text="Detalhar", command=detalhar)
# btn_visu.grid(row=1,column=1,stick = "e")

principal.mainloop()