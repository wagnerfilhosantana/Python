from tkinter import *

aplication = Tk()
aplication.title('app')
aplication.geometry('640x400')

def Senha():
    print(f'Senha: {vsenha.get()}')

vsenha = StringVar()

p_senha = Entry(aplication, textvariable= vsenha, show= '*')
p_senha.pack()

button = Button(aplication, text = "login", command= Senha)
button.pack()
    
aplication.mainloop()