import re 

texto = 'Estou fazendo um curso de Python...'
print(f'TEXTO: {texto}')

def AnwserText(word, OtherThing):
    anwser = re.sub(word, OtherThing, texto)
    return anwser

def Espace():
    return print('-'*10)

while True:
    Espace()
    word = str(input('Digite qual caractere para substituir: '))
    OtherThing = str(input('Digite o caractere para substituir: '))
    anwser = AnwserText(word, OtherThing)
    Espace()

    print(anwser)
    Espace()