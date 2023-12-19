from tkinter import *

aplication = Tk()
aplication.title('Exemplo Grid')
aplication.geometry('400x200')

vesprotes = StringVar()
listaEsporte = ['Futebol', 'Volei', 'Basquete']
vesprotes.set(listaEsporte[0])

esportes = Label(aplication, text = 'Esportes')
esportes.pack()

op_esportes = OptionMenu(aplication, vesprotes, *listaEsporte)
op_esportes.pack()

btn_esporte = Button(aplication, text = 'Esporte selecionado')
btn_esporte.pack()

aplication.mainloop()