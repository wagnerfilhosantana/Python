import sqlite3
from sqlite3 import Error

def ConnectionBase():
    caminho = 'C:\\Users\\wagne\\OneDrive\\Documentos\\GitHub\\Python\\Banco de Dados\\agenda.db'
    try: 
        connection = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    
    return connection

vsql = """CREATE TABLE ContatosClientes(
    IDCLIENTE INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMECLIENTE VARCHAR(30),
    TELEFONECLIENTE VARCHAR(14),
    EMAILCLIENTE VARCHAR(30)
);"""

vcon = ConnectionBase()

def CreateBase(connecton, sql):
    try:
        construtor = connecton.cursor()
        construtor.execute(sql)
        print('Tabela criada.')
    except Error as ex:
         print(ex)

CreateBase(vcon, vsql)
vcon.close()
    