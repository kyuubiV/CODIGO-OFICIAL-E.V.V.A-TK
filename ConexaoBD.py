import sqlite3

bancodados = "bando.bd"

def iniciar_conexao():
  conexao = None
  try:
    conexao = sqlite3.connect(bancodados) 
    print("Conexão concluída.")
  except sqlite3.Error as e:
    print("Erro de conexão.",e)
  return conexao
variconexao = iniciar_conexao()
#Criar Tabela
def newTable(conexao,sql):
  try:
    cursor = conexao.cursor()
    cursor.execute(sql)
    print("Tabela criada com sucesso!")
  except sqlite3.Error as e:
    print("Erro ao criar a tabela", e)

def insert(conexao,sql):
  try:
    cursor = conexao.cursor()
    cursor.execute(sql)
    conexao.commit()
    print("Dados adicionados com sucesso.")
  except sqlite3.Error as  e:
    print("Erro ao adicionar dados.",e)

def select(conexao,sql):
  try:
    cursor = conexao.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    return resultado
  except sqlite3.Error as e:
    print("Erro ao selecionar dados.",e)

def update(conexao,sql):
  try:
    cursor = conexao.cursor()
    cursor.execute(sql)
    conexao.commit()
    print("Dados Atualizados com sucesso")
  except sqlite3.Error as e:
    print("Erro em atualizar dados.",e)
    
def delete(conexao,sql):
  try:
    cursor = conexao.cursor()
    cursor.execute(sql)
    conexao.commit()
    print("Dados deletados.")
  except sqlite3.Error as e:
    print("Erro ao deletar Dados.",e)