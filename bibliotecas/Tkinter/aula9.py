from tkinter import *
from tkinter import messagebox

aplication = Tk()
aplication.title('app')
aplication.geometry('400x150')

def mostrarMsg(tipomsg, msg):
    if (tipomsg == '1'):
        messagebox.showinfo(title = 'CFB cursos', message= msg)
    elif tipomsg == '2':
        messagebox.showwarning(title = 'CFB cursos', message= msg)
    elif tipomsg == '3':
        messagebox.showerror(title = 'CFB cursos', message= msg)



vmsg = ' Curso de Python com Tkinter.'
vnum_cstexto = StringVar()

Label(aplication, text= 'Tipo de caixa(1, 2 ou 3)').pack()
tb_num = Entry(aplication, textvariable= vnum_cstexto)
vnum_cstexto.set('1')
tb_num.pack()

btn_msg = Button(aplication, text= 'Mostrar mensagem', command= lambda: mostrarMsg(vnum_cstexto.get(), vmsg))
btn_msg.pack()
    
aplication.mainloop()