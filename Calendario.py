from Atividade import *
from ConexaoBD import *
from Banco import *
import tkinter.messagebox
from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from ConexaoBD import *
import calendar 
from datetime import *

class Calendario:
  def __init__(self):
    self.dia = StrVar()
    self.mes = StrVar()
    self.ano = StrVar()
    self.hora = StrVar()
    self.atividade = None
