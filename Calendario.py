from Atividade import *

# Meses
jan = {} 
fev = {}
mar = {}
abr = {}
maio = {}
jun = {} 
jul = {} 
ago = {} 
semp = {} 
out = {}
nov = {} 
dez = {}

# Classe 
class Calendario:
  def __init__(self):
    self.dia = None
    self.mes = None
    self.ano = None
    self.tempo = None
    self.atividade = None
    
  # Organização das atividades em meses 
  def AgendarAtividade(self):
    try:
      self.dia = int(input("Insira o dia: "))
      self.mes = int(input("Insira o mês: "))
      self.ano = int(input("Insira o ano: "))
      self.hora = input("Insira o horário(00:00): ")
      self.atividade = Atividades()
      
    # Organização das atividades em meses 
      if self.mes == 1:
       jan[self.dia,self.mes,self.ano,self.hora] = self.atividade.editarAtividade(),self.atividade.GetLocal()
      elif self.mes == 2:
       fev[self.dia,self.mes,self.ano,self.hora] = self.atividade.editarAtividade(),self.atividade.GetLocal()
      elif self.mes == 3:
       mar[self.dia,self.mes,self.ano,self.hora] = self.atividade.editarAtividade(),self.atividade.GetLocal()
      elif self.mes == 4:
       abr[self.dia,self.mes,self.ano,self.hora] = self.atividade.editarAtividade(),self.atividade.GetLocal()
      elif self.mes == 5:
        maio[self.dia,self.mes,self.ano,self.hora] = self.atividade.editarAtividade(),self.atividade.GetLocal()
      elif self.mes == 6:
        jun[self.dia,self.mes,self.ano,self.hora] = self.atividade.editarAtividade(),self.atividade.GetLocal()
      elif self.mes == 7:
        jul[self.dia,self.mes,self.ano,self.hora] = self.atividade.editarAtividade(),self.atividade.GetLocal()
      elif self.mes == 8:
        ago[self.dia,self.mes,self.ano,self.hora] = self.atividade.editarAtividade(),self.atividade.GetLocal()
      elif self.mes == 9:
        semp[self.dia,self.mes,self.ano,self.hora] = self.atividade.editarAtividade(),self.atividade.GetLocal()
      elif self.mes == 10:
        out[self.dia,self.mes,self.ano,self.hora] = self.atividade.editarAtividade(),self.atividade.GetLocal()
      elif self.mes == 11:
        nov[self.dia,self.mes,self.ano,self.hora] = self.atividade.editarAtividade(),self.atividade.GetLocal()
      elif self.mes == 12:
        dez[self.dia,self.mes,self.ano,self.hora] = self.atividade.editarAtividade(),self.atividade.GetLocal()
      else:
        print("Não encontramos um mês correspondente.")
        return print("Falha no Agendamento.")
      per = input("Deseja adicionar uma pasta de recado?(s/n): ")
      if per == "s":
       self.atividade.adicionar_comentario()       
      return print("Agendamento realizado.")
    except ValueError:
      print("A data é em valor númerico.Ex: Dia = 25\nJaneiro = 01\n Ano = 2022")
      return print("Falha no Agendamento.")
    
    
      
      # Exibir as atividades do Usuário de acordo com o mês
  def exibircalendario(self):
    mes = int(input("Qual mês você deseja visualizar? "))
    if mes == 1:
       print("Atividades: \n")
       for key in jan:
        print('Atividade e Local:',jan[key],f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3])
    elif mes == 2:
       print("Atividades: \n")
       for key in fev:
        print('Atividade e Local:',fev[key],f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3])
    elif mes == 3:
       print("Atividades: \n")
       for key in mar:
        print('Atividade e Local:',mar[key],f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3])   
    elif mes == 4:
       print("Atividades: \n")
       for key in abr:
        print('Atividade e Local:',abr[key],f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3])
    elif mes == 5:
       print("Atividades: \n")
       for key in maio:
        print('Atividade e Local:',maio[key],f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3])
    elif mes == 6:
       print("Atividades: \n")
       for key in jun:
        print('Atividade e Local:',jun[key],f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3])
    elif mes == 7:
       print("Atividades: \n")
       for key in jul:
        print('Atividade e Local:',jul[key],f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3])
    elif mes == 8:
       print("Atividades: \n")
       for key in ago:
        print('Atividade e Local:',ago[key],f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3])
    elif mes == 9:
       print("Atividades: \n")
       for key in semp:
        print('Atividade e Local:',semp[key],f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3])
    elif mes == 10:
       print("Atividades: \n")
       for key in out:
        print('Atividade e Local:',out[key],f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3])
    elif mes == 11:
       print("Atividades: \n")
       for key in nov:
        print('Atividade e Local:',nov[key],f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3])
    elif mes == 12:
       print("Atividades: \n")
       for key in dez:
        print('Atividade e Local:',dez[key],f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3])

  # Buscar a ativide escolida pelo Usuário no Calendário
  def BuscarAtividade(self):
   Atv = input("Qual o nome da Atividade? ")
  
    # Janeiro
   for key in jan:
     if Atv in jan[key]:
       print(f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3],'\nAtividade e Local:',jan[key])
       
   # Fevereiro
   for key in fev:
    if Atv in fev[key]:
      print(f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3],'\nAtividade e Local:',fev[key])
      
    # Março
   for key in mar:
    if Atv in mar[key]:
      print(f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3],'\nAtividade e Local:',mar[key])
      
    # Abril
   for key in abr:
    if Atv in abr[key]:
      print(f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3],'\nAtividade e Local:',abr[key])
      
   # Maio
   for key in maio:
    if Atv in maio[key]:
      print(f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3],'\nAtividade e Local:',maio[key])
      
  # Junho
   for key in jun:
    if Atv in jun[key]:
      print(f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3],'\nAtividade e Local:',jun[key])
      
  # Julho 
   for key in jul:
     if Atv in jul[key]:
      print(f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3],'\nAtividade e Local:',jul[key])
       
  # Agosto
   for key in ago:
     if Atv in ago[key]:
      print(f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3],'\nAtividade e Local:',ago[key])
       
   # Setembro
   for key in semp:
     if Atv in semp[key]:
      print(f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3],'\nAtividade e Local:',semp[key])
       
    # Outubro
   for key in out:
    if Atv in out[key]:
      print(f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3],'\nAtividade e Local:',out[key])
      
    # Novembro
   for key in nov:
    if Atv in nov[key]:
      print(f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3],'\nAtividade e Local:',nov[key])
      
  # Dezembro
   for key in dez:
    if Atv in dez[key]:
      print(f'\nData:{key[0]}/{key[1]}/{key[2]}',"\nHorário:",key[3],'\nAtividade e Local:',dez[key])
      