import re 

texto = 'Estou fazendo um curso de Python...'

while True:
    a = input('Digite a palavra que voce queira procurar:')
    res =  re.findall(a, texto)

    print(res)