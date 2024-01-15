from tkinter import *

aplication = Tk()
aplication.title('app')
aplication.geometry('640x400')

def valorEscola():
    print('Valor da escala: ' + str(sc_scale.get()))

lb_valor = Label(aplication, text = 'Valor')
lb_valor.pack()

sc_scale = Scale(aplication, from_= 0, to = 100, orient = HORIZONTAL)
sc_scale.set(50)
sc_scale.pack()

botao = Button(aplication, text = 'Valor Escala', command= valorEscola)
botao.pack()


aplication.mainloop()