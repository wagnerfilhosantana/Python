from tkinter import *
from tkinter import ttk

aplication = Tk()
aplication.title('app')
aplication.geometry('640x400')

def escolherEsportes():
    ve = cb_esportes.get()
    print('Esporte: ' + ve)

listaEsportes = ['futebol', 'Volei', 'Basquete']

lb_esportes = Label(aplication, text = 'Esportes')
lb_esportes.pack()

cb_esportes = ttk.Combobox(aplication, values = listaEsportes)
cb_esportes.set('Futebol')
cb_esportes.pack()

butao = Button(aplication, text = 'Escolher', command= escolherEsportes)
butao.pack()


aplication.mainloop()