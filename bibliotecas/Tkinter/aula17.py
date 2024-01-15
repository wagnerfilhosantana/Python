from tkinter import *

aplication = Tk()
aplication.title('app')
aplication.geometry('600x400')

def selectionEsport():
    print("Esporte: " + str(esporte.get(ACTIVE)))

def addEsporte():
    esporte.insert(END, vnovoEsporte.get())

def ImpVal():
    print("Valor selecionado:" + sp_valores2.get())

# LabelFrame
labelframe = LabelFrame(aplication, text= 'Esportes', borderwidth= 1, relief= 'solid')
labelframe.place(x = 10, y = 10, width= 200, height= 150)

#ListBox
listaEsportes = ['Futebol', 'Volei', 'Basquete', 'Tenis']
esporte = Listbox(aplication)

for esp in listaEsportes:
    esporte.insert(END, esp)
esporte.pack()

btn_esporte = Button(aplication, text = "Imprimir esporte", command = selectionEsport)
btn_esporte.pack()

vnovoEsporte = Entry(aplication)
vnovoEsporte.pack()

btn_inserir = Button(aplication, text = 'Inserir Esporte', command = addEsporte)
btn_inserir.pack()

#Spinbox
sp_valores = Spinbox(labelframe, from_ = 0, to = 100)#Primeira Forma: Qual o valor maior e qual e o valor menor
sp_valores.pack()

sp_valores2 = Spinbox(labelframe, values = (1,2,3,4,5))
sp_valores2.pack()

btn_valor = Button(labelframe, text = 'Imprimir valor', command= ImpVal)
btn_valor.pack()
aplication.mainloop()