from tkinter import *

aplication = Tk()
aplication.title('app')
aplication.geometry('640x400')

vfutebol = StringVar
vbasquete = StringVar
vvolei = StringVar

fr_quadrado = Frame(aplication, borderwidth= 0.5, relief= 'sunken') # relef( flat, solid, raised, sunken)
fr_quadrado.place(x = 5, y = 5, width = 250, height= 75)

fb_futebol = Checkbutton(fr_quadrado, text = 'Futebol', variable= vfutebol, onvalue= 's', offvalue='n')
fb_futebol.pack(side = LEFT)
fb_volei = Checkbutton(fr_quadrado, text = 'Vôlei', variable= vvolei, onvalue= 's', offvalue='n')
fb_volei. pack(side = LEFT)
fb_basquete = Checkbutton(fr_quadrado, text = 'Basquete', variable= vbasquete, onvalue= 's', offvalue='n')
fb_basquete.pack(side = LEFT)
    
aplication.mainloop()