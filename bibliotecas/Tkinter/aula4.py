from tkinter import *
import os
import Banco
import sqlite3
from sqlite3 import Error

aplication = Tk()
def ConnectionBase():
    caminho = 'C:\\Users\\wagne\\OneDrive\\Documentos\\GitHub\\Python\\Banco de Dados\\agenda.db'
    try: 
        connection = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    
    return connection

aplication.title('Alpication')
aplication.geometry('500x300')
aplication.configure(background= '#dde')

def Dateprint():
    if tb_name.get() != "":
        vnome = tb_name.get()
        vphone = tb_phone.get()
        vemail = tb_email.get()
        vobs = tb_obs.get('1.0', END)
        vquery = "INSERT INTO ContatosClientes (NOMECLIENTE, TELEFONECLIENTE, EMAILCLIENTE, OBSCLIENT) VALUES('"+vnome+"', '"+vphone+"', '"+vemail+"', '"+vobs+"')"
        Banco.dml(vquery)
        tb_name.delete(0,END)
        tb_phone.delete(0,END)
        tb_email.delete(0,END)
        tb_obs.delete('1.0',END)
        print('Dados gravados')
    else:
        print('Erro!')



text = Label(aplication, text = 'Name:', background= '#ddd', foreground= '#009', anchor= W)
text.place(x = 10,y = 10, width = '100', height= '20')

tb_name = Entry(aplication)
tb_name.place(x = 10, y = 30, width = 150, height = 20)

text = Label(aplication, text = 'Number Phone:', background= '#ddd', foreground= '#009', anchor= W)
text.place(x = 10,y = 70, width = '100', height= '20')

tb_phone = Entry(aplication)
tb_phone.place(x = 10, y = 90, width = 150, height = 20)

text = Label(aplication, text = 'E-mail:', background= '#ddd', foreground= '#009', anchor= W)
text.place(x = 10,y = 130, width = '100', height= '20')

tb_email = Entry(aplication)
tb_email.place(x = 10, y = 150, width = 150, height = 20)

text = Label(aplication, text = 'OBS:', background= '#ddd', foreground= '#009', anchor= W)
text.place(x = 10,y = 180, width = '100', height= '20')

tb_obs = Text(aplication)
tb_obs.place(x = 10, y =200, width = 150, height = 50)

btn = Button(aplication, text = 'Send', command = Dateprint)
btn.place(x = 110, y = 250, width = 50, height= 20) 

aplication.mainloop()