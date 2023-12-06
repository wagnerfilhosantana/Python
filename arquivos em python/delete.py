import os

wayFile = 'C:/Users/wagne/OneDrive/Documentos/GitHub/Python/arquivos em python/'
readFile = 'text.txt'

file = open(wayFile + readFile, 'x')
file.close()

os.remove(wayFile + readFile)
