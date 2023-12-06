import re 

texto = 'Estou fazendo um curso de Python...'
print(f'TEXTO: {texto}')

def answerText(a):
    
   
    res = re.search(a, texto)
    Espace()
    print(res.start())
    Espace()
    print(res.end())
    Espace()
    return res

def Espace():
    return print('-'*10)

while True:
    Espace()
    a = str(input('Digite a palavra que queira ver as ocorrencias: '))
    
    answerText(a) 