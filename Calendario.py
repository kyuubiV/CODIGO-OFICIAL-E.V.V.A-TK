from Atividade import *
from ConexaoBD import *
from Banco import *

newTable(variconexao,tabelaCalendario)


class Calendario:
  def __init__(self):
    self.dia = None
    self.mes = None
    self.ano = None
    self.tempo = None
    self.atividade = None
  def AgendarAtividade(self):
    try:
      self.dia = int(input("Insira o dia: "))
      self.mes = int(input("Insira o mês: "))
      self.ano = int(input("Insira o ano: "))
      self.hora = input("Insira o horário(00:00): ")
      self.atividade = Atividades()
      insert(variconexao,("INSERT INTO calendario(dia,mes,ano,horario) VALUES ('"+self.dia+"','"+self.mes+"','"+self.ano+"','"+sel.hora+"')); "))