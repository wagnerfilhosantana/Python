def verificar(n):
    if n > 0:
        print('POSITIVO!')
    elif n == 0:
        print('NULO!')
    else: 
        print('NEGATIVO!')

def menu():

    n = int(input('Digite um numero: '))
    verificar(n)

while True:
    menu()