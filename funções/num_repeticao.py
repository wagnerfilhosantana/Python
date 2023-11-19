def num_repeticao(n):
    for i in range(1, n+1):
        cont = 1
        while True:
            print(i, end= ' ')
            if cont == i:
                break
            cont += 1
        print()

def menu():
    n = int(input('Digite um numero: '))
    num_repeticao(n)

while True:
    menu()