import os 
import sqlite3
from sqlite3 import Error

def ConnectionBase():
    caminho = 'C:\\Users\\wagne\\OneDrive\\Documentos\\GitHub\\Python\\Banco de Dados\\agenda.db'
    try: 
        connection = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return connection

vconnection = ConnectionBase()

def query(conexao, sql):
    try:
        construtor = conexao.cursor()
        construtor.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Operacao realizada com sucesso!')

def Select(conexao, sql):
    construtor = conexao.cursor()
    construtor.execute(sql)
    res = construtor.fetchall()
    return res

def PrincipalHome():
    os.system('cls')
    print('1 - Inserir Registro')
    print('2 - Deletar Registro')
    print('3 - Alterar Registro')
    print('4 - Consultar Registro por ID')
    print('5 - Consultar Registro por nome')
    print('6 - Sair')

def InsertHome():

    os.system('cls')
    nome = input('Digite seu nome: ')
    telefone = input('Digite seu telefone: ')
    email = input('Digite seu email: ')
    vsql = "INSERT INTO ContatosClientes(NOMECLIENTE,TELEFONECLIENTE,EMAILCLIENTE)VALUES('"+nome+"', '"+telefone+"', '"+email+"')"
    query(vconnection, vsql)

def DeleteHome():

    os.system('cls')
    IDnumber = input('Digite o ID: ')
    vsql = "DELETE FROM ContatosClientes WHERE IDCLIENTE = '"+IDnumber+"'"
    query(vconnection, vsql)

def UpdateHome():
    
    os.system('cls')
    clientId = input('Digite o numero do ID: ')

    result = Select(vconnection, "SELECT * FROM ContatosClientes WHERE IDCLIENTE = "+clientId+"")
    resultname = result[0][1]
    resultnumber = result[0][2]
    resultemail = result[0][3]

    clientname = input('Digite o nome do cliente: ')
    numberclient = input('Digite o numero de telefone: ')
    emailclient = input('Digite o email: ')

    if (len(clientname) == 0):
        clientname = resultname
    if (len(numberclient) == 0):
        numberclient = resultnumber
    if (len(clientname) == 0):
        clientname = resultemail
    
    vsql = "UPDATE contatosClientes SET NOMECLIENTE = '"+clientname+"', TELEFONECLIENTE = '"+numberclient+"', EMAILCLIENTE = '"+emailclient+"' WHERE IDCLIENTE = '"+clientId+"'"
    query(vconnection, vsql)
    

    

def SelectHomeID():

    os.system('cls')
    vsql = "SELECT * FROM contatosClientes"
    result = Select(vconnection, vsql)
    lim = 10 
    cont = 0
    for r in result:
        print('ID: {0:_<3} Nome: {1:_<30} Telefone: {2:_<14} E-mail: {3:_<30}'.format(r[0],r[1],r[2],r[3]))
        cont += 1
        if (cont >= lim):
            cont = 0 
            os.system("PAUSE")
            os.system('cls')
    print('Fim da lista!')
    os.system('PAUSE')

def SelectHomename():

    os.system('cls')
    clientname = input('Digite o nome do cliente: ')
    vsql = "SELECT * FROM contatosClientes WHERE NOMECLIENTE LIKE '%"+clientname+"%'"
    result = Select(vconnection, vsql)
    lim = 10 
    cont = 0
    for r in result:
        print('ID: {0:_<3} Nome: {1:_<30} Telefone: {2:_<14} E-mail: {3:_<30}'.format(r[0],r[1],r[2],r[3]))
        cont += 1
        if (cont >= lim):
            cont = 0 
            os.system("PAUSE")
            os.system('cls')
    print('Fim da lista!')
    os.sytem('PAUSE')

opcion = 0
while opcion != 6:
    PrincipalHome()
    opcion = int(input('digite uma opcao: '))

    if opcion == 1:
        InsertHome()
    elif opcion == 2:
        DeleteHome()
    elif opcion == 3:
        UpdateHome()
    elif opcion == 4:
        SelectHomeID()
    elif opcion == 5:
        SelectHomename()
    else:
        print('Obrigado por usar nosso app!')