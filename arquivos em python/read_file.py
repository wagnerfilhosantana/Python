
wayFile = 'C:/Users/wagne/OneDrive/Documentos/GitHub/Python/arquivos em python/'
readFile = 'readtext.txt'

def WriteFile():
    file = open(wayFile + readFile, 'wt')
    i = 1
    while i <= 2:
        txt = input('Digite um texto: ')
        file.write(f'{txt}\n')
        i += 1
    return file

def Space():
    print('-'*50)
WriteFile()
Space()

file = open(wayFile + readFile, 'rt')


for l in file:
    print(l)
    Space()

print(file.read())
Space()

print(file.readline())
Space()
file.close()