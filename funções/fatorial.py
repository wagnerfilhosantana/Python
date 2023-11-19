def fatorial(n):
    i = 1
    res = 1
    while i <= n:
        res *= i
        i += 1
    return res

def menu():
    n = float(input('Digite um numero: '))
    fat = fatorial(n)
    print(f'O fatorial de {n} e igual a {fat}')

while True:
    menu()