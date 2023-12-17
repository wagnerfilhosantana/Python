from tkinter import *
import os

def semcomando():
    print('sem comando')

def Formulario():
    return 'C:\\Users\\wagne\\OneDrive\\Documentos\\GitHub\\Python\\bibliotecas\\Tkinter\\aula4.py'

def OpenFormulario():
    exec(open(Formulario()).read())

os.system('cls')

aplication = Tk()
aplication.title('App')
aplication.geometry('500x300')
aplication.configure(background= '#dde')

BarraDeMenu = Menu(aplication)
menuContatos = Menu(BarraDeMenu, tearoff= 0)
menuContatos.add_command(label = 'Novo', command= OpenFormulario)
menuContatos.add_command(label = 'Pesquisar', command= semcomando)
menuContatos.add_command(label = 'Deletar', command= semcomando)
menuContatos.add_separator()
menuContatos.add_command(label = 'Sair', command= aplication.quit)
BarraDeMenu.add_cascade(label= 'contatos', menu= menuContatos)

aplication.config(menu = BarraDeMenu)

aplication.mainloop()