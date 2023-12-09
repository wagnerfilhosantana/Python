import sqlite3
from sqlite3 import Error

def ConnectionBase():
    caminho = 'C:\\Users\\wagne\\OneDrive\\Documentos\\GitHub\\Python\\Banco de Dados\\agenda.db'
    try: 
        connection = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    
    return connection

vcon = ConnectionBase()

nome = input('Digite seu nome: ')
telefone = input('Digite seu telefone: ')
email = input('Digite seu email: ')
vsql = "INSERT INTO ContatosClientes(NOMECLIENTE,TELEFONECLIENTE,EMAILCLIENTE)VALUES('"+nome+"', '"+telefone+"', '"+email+"')"

def inserir(conexao, sql):
    try:
        construtor = conexao.cursor()
        construtor.execute(sql)
        conexao.commit()
        print('Registro inserido')
    except Error as ex:
        print(ex)

inserir(vcon, vsql)
vcon.close()

