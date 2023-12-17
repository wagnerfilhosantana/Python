from tkinter import *
import os

aplication = Tk()
way = os.path.dirname(__file__)

namefile = way + '\\name.txt'

aplication.title('Alpication')
aplication.geometry('500x300')
aplication.configure(background= '#dde')

def Dateprint():
    os.system('cls')
    file = open(namefile, "a")
    file.write('\nName: %s' % name.get())
    file.write('\nPhone Number: %s' % phone.get())
    file.write('\nE-mail: %s' % email.get())
    file.write('\nObs: %s' % obs.get('1.0', END))
    file.write('\n\n')
    file.close

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

btn = Button(aplication, text = 'Send', command = Dateprint)
btn.place(x = 110, y = 250, width = 50, height= 20) 

aplication.mainloop()