from tkinter import *
from tkinter import ttk

aplication = Tk()
aplication.title('app')
aplication.geometry('600x400')

nb = ttk.Notebook(aplication)
nb.place(x = 0, y = 0, width = 300, height= 200)

tb1 = Frame(nb)
nb.add(tb1, text = "cursos de Python")
tb2 = Frame(nb)
nb.add(tb2, text = "Sobre mim")
tb3 = Frame(nb)
nb.add(tb3, text = "Saber mais")

lb1 = Label(tb1, text = "É um otimo curso.")
lb1.pack()
lb2 = Label(tb2, text = "Estou estando Python.")
lb2.pack()
lb3 = Label(tb3, text = "Clique aqui para mais informacao")
lb3.pack()


aplication.mainloop()