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