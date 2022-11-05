from ConexaoBanco import *

tabelaUsuario = """CREATE TABLE IF NOT EXISTS usuario(
id_user integer not null primary key autoincrement,
cpf varchar(11) not null,
email varchar(256) not null,
senha varchar(8),
nome_user varchar(30),
telefone varchar(12),
data_aniver date
);"""

tabelaCalendario = """CREATE TABLE IF NOT EXISTS calendario(
id_calen integer not null primary key auto_increment,
dia integer(2) not null,
mes integer(2) not null,
ano integer(4) not null,
horario time,
);
"""

tabelaAtividade = """create table if not exists atividade(
id_ativ integer not null auto_increment,
id_calen integer,
nome_atividade varchar(30) not null,
tipo_atividade varchar(20) not null,
local_atividade varchar(30),
comentario text,
foreign key(id_calen)
references calendario(id_calen);
primary key(id_ativ)
);
"""

tabelaTem = """create table if not exists tem(
id_user integer,
id_cale integer,
foreign key(id_user)
references usuario(id_user),
foreign key(id_calen)
references calendario(id_calen));
"""

# Teste do Banco

# cpf = input("Digite seu CPF: ")
# email = input("Insira seu e-mail: ")
# senha = input("Insira uma senha(max 8 digitos): ")
# nome_user = input("Insira seu nome de usuario: ")
# telefone = input("Insira seu telefone: ")
# dia = input("digite o dia do aniversário: ")
# mes = input("digite o mes do aniversário: ")
# ano = input("digite o ano do aniversário: ")


# insert_sql = "INSERT INTO usuario (cpf, email,senha,nome_user,telefone,data_Aniver) VALUES ('"+cpf+"','"+email+"','"+senha+"','"+nome_user+"','"+telefone+"','"+ano+mes+dia+"');"
# insert(variconexao,insert_sql)
