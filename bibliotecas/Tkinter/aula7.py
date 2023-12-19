from tkinter import *

aplication = Tk()
aplication.title('Exemplo Grid')
aplication.geometry('400x200')

vesprotes = StringVar()

def SelectionEsport():
    ve = vesprotes.get()
    if ve == 'f':
        print('Futebol')
    elif ve == 'v':
        print('Voleibol')
    else:
        print('Basquetebol')
    

esportes = Label(aplication, text = 'Esportes')
esportes.pack()

futebol = Radiobutton(aplication, text = 'Futebol', value = 'f', variable= vesprotes)
futebol.pack()

volei = Radiobutton(aplication,text = 'Vôlei', value = 'v', variable= vesprotes)
volei.pack()

basquete = Radiobutton(aplication,text = 'Basquete', value = 'b', variable= vesprotes)
basquete.pack()

btn_esporte = Button(aplication, text = 'Esporte selecionado', command = SelectionEsport)
btn_esporte.pack()

aplication.mainloop()
