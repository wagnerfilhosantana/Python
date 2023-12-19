from tkinter import *

aplication = Tk()
aplication.geometry('150x250')
aplication.title('IMC calculator')
aplication.configure(background= '#dde')

def IMC_calculator():
    peso = int(tb_peso.get())
    altura = float(tb_altura.get())
    imc = peso/(altura*2)
    resultado['text'] = f"Seu IMC é {imc:.2f}"

text = Label(aplication, text = 'digite seu peso:', background= '#ddd', foreground= '#009', anchor= W)
text.place(x = 10,y = 10, width = '100', height= '20')

tb_peso = Entry(aplication)
tb_peso.place(x = 10, y = 30, width = 120, height = 20)

text = Label(aplication, text = 'Digite sua altura:', background= '#ddd', foreground= '#009', anchor= W)
text.place(x = 10,y = 50, width = '100', height= '20')

tb_altura = Entry(aplication)
tb_altura.place(x = 10, y = 70, width = 120, height = 20)

resultado = Label(aplication, text = '', background = '#dde', foreground = "#000", anchor = W)
resultado.place(x = 10, y = 95, width = 100, height = 20)

btn = Button(aplication, text = 'Calcular', command = IMC_calculator)
btn.place(x = 45, y = 150, width = 50, height= 20) 

aplication.mainloop()
