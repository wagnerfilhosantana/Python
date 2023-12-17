from tkinter import *
import os

aplication = Tk()

def semcomando():
    print('sem comando')

aplication.title('Alpication')
aplication.geometry('500x300')
aplication.configure(background= '#dde')

BarraDeMenu = Menu(aplication)
menuContatos = Menu(BarraDeMenu, tearoff= 0)
menuContatos.add_command(label = 'Novo', command= semcomando)
menuContatos.add_command(label = 'Pesquisar', command= semcomando)
menuContatos.add_command(label = 'Deletar', command= semcomando)
menuContatos.add_separator()
menuContatos.add_command(label = 'Sair', command= aplication.quit)
BarraDeMenu.add_cascade(label= 'contatos', menu= menuContatos)

menumanutensao = Menu(BarraDeMenu, tearoff= 0)
menumanutensao.add_command(label = 'Banco de Dados', command= semcomando)
BarraDeMenu.add_cascade(label = 'Manutensão', menu = menumanutensao)

aplication.config(menu = BarraDeMenu)



aplication.mainloop()