wayFile = 'C:/Users/wagne/OneDrive/Documentos/GitHub/Python/arquivos em python/'
newFile = 'file.txt'

file = open(wayFile + newFile, 'wt')
i = 1
while i <= 3:
    txt = input('Digite um texto: ')
    file.write(f'{txt}\n')
    i += 1
