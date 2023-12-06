import re 

texto = 'Estou fazendo um curso de Python...'
print(f'TEXTO: {texto}')

def AnwserText(word):
    anwser = re.split(word, texto)
    return anwser

def Espace():
    return print('-'*10)

while True:
    Espace()
    word = str(input('Digite a palavra que queira tornar uma lista: '))
    anwser = AnwserText(word)
    Espace()

    print(anwser)
    Espace()

    for t in AnwserText(word):
        print(t)
    