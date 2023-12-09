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

def atualizar(conexao, sql):
    try:
        construtor = conexao.cursor()
        construtor.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Registro atualizado')

vsql = "UPDATE contatosClientes SET NOMECLIENTE = 'Clenilce', TELEFONECLIENTE = '(43) 97654-1234' WHERE IDCLIENTE = 1"
atualizar(vcon, vsql)

vcon.close()