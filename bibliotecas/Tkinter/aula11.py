from tkinter import *
from tkinter import messagebox

aplication = Tk()
aplication.title('app')
aplication.geometry('400x150')

def mostrarMsg():
    messagebox.showinfo(title = 'CFB cursos', message= 'Curso de Python!')
    
vnum_cstexto = StringVar()

fr_quadrado = Frame(aplication, borderwidth= 0.5, relief= 'sunken') # relef( flat, solid, raised, sunken)
fr_quadrado.place(x = 5, y = 5, width = 150, height= 75)

Label(fr_quadrado, text= 'Tipo de caixa(1, 2 ou 3)').pack()
tb_num = Entry(fr_quadrado, textvariable= vnum_cstexto)
vnum_cstexto.set('1')
tb_num.pack()

label = Label(aplication, text= 'Curso de Python no tkinter.', font=('Arial', 15))
label.pack(side = RIGHT, fill = X, expand = TRUE)

btn_msg = Button(fr_quadrado, text= 'Mostrar mensagem', command= mostrarMsg)
btn_msg.pack()
    
aplication.mainloop()