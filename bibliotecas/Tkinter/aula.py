from tkinter import *

aplication = Tk()

aplication.title('My first software')
aplication.geometry('500x300')
aplication.configure(background = "#008")

text = Label(aplication, text = 'Curso de python',background = "#ff0", foreground= "#000")
text.place(x = 10, y = 10, width = 100, height= 15)

vtxt = 'Modulo tkinter'
vbg = '#ff0'
vfg = '#000'

texttwo = Label(aplication, text = vtxt, bg = vbg, fg = vfg)
texttwo.pack(ipadx = 20, ipady = 20, padx = 5, pady = 5, side = 'bottom', fill = X, expand = True)

aplication.mainloop()