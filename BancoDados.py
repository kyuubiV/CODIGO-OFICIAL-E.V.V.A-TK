import sqlite3
from sqlite3 import Error

arquivo = "bando.bd"

def conexao(arquivo):
  conexao = None
  try:
    conexao=sqlite3.connect(arquivo)
    print("Conexão realizada com sucesso.")
  except Error as e:
    print("Erro ao conectar banco de dados.", e)
  return conexao
variconexao = conexao(arquivo)


  
