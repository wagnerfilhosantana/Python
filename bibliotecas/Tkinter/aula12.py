from tkinter import *

aplication = Tk()
aplication.title('app')
aplication.geometry('640x400')

img = PhotoImage(file = "C:\\Users\\wagne\\OneDrive\\Documentos\\GitHub\\Python\\bibliotecas\\Tkinter\\img_godwolf.png")
imagem = Label(aplication, image= img)
imagem.pack()
    
aplication.mainloop()