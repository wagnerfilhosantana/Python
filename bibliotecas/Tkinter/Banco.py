import sqlite3
from sqlite3 import Error


def ConnectionBase():
    caminho = 'C:\\Users\\wagne\\OneDrive\\Documentos\\GitHub\\Python\\Banco de Dados\\agenda.db'
    try: 
        connection = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    
    return connection

def dql(query):
    vcon = ConnectionBase()
    c = vcon.cursor()
    c.execute(query) 
    res = c.fetchall()
    vcon.close()
    return res

def dml(query):
    try: 
        vcon = ConnectionBase()
        c = vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(f'Erro de execusao: {ex}')

 
