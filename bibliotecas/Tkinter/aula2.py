from tkinter import *

aplication = Tk()

aplication.title('Alpication')
aplication.geometry('500x300')
aplication.configure(background= '#dde')

text = Label(aplication, text = 'Name:', background= '#ddd', foreground= '#009', anchor= W)
text.place(x = 10,y = 10, width = '100', height= '20')

name = Entry(aplication)
name.place(x = 10, y = 30, width = 150, height = 20)

text = Label(aplication, text = 'Number Phone:', background= '#ddd', foreground= '#009', anchor= W)
text.place(x = 10,y = 70, width = '100', height= '20')

phone = Entry(aplication)
phone.place(x = 10, y = 90, width = 150, height = 20)

text = Label(aplication, text = 'E-mail:', background= '#ddd', foreground= '#009', anchor= W)
text.place(x = 10,y = 130, width = '100', height= '20')

email = Entry(aplication)
email.place(x = 10, y = 150, width = 150, height = 20)

text = Label(aplication, text = 'OBS:', background= '#ddd', foreground= '#009', anchor= W)
text.place(x = 10,y = 180, width = '100', height= '20')

obs = Text(aplication)
obs.place(x = 10, y =200, width = 150, height = 50)

aplication.mainloop()
