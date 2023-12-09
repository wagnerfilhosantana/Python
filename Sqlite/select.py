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

def consultar(conexao, sql):

    construtor = conexao.cursor()
    construtor.execute(sql)
    resultado = construtor.fetchall()
    return resultado

vsql = "SELECT * FROM contatosClientes WHERE NOMECLIENTE = 'Clenilce'"

res = consultar(vcon, vsql)
for r in res:
    print(r)