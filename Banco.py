from ConexaoBD import *

tabelaUsuario = """CREATE TABLE IF NOT EXISTS usuario(
id_user integer not null primary key autoincrement,
email varchar(256) not null,
senha varchar(8),
nome_user varchar(30),
telefone varchar(12),
data_aniver date
);"""
# newTable(variconexao,tabelaUsuario)
  
tabelaCalendario = """CREATE TABLE IF NOT EXISTS calendario
(id_calen integer not null primary key autoincrement,
id_user integer,
dia integer(2) not null,
mes integer(2) not null,
ano integer(4) not null,
horario time,
nome_atividade varchar(30) not null,
tipo_atividade varchar(20) not null,
local_atividade varchar(30),
comentario text,
foreign key(id_user)
references usuario (id_user)
);"""

# newTable(variconexao,tabelaCalendario)

