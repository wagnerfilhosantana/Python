
def perfect(n):
    soma = 0
    for val in range(1,n):
        if n % val == 0:
            soma += val

    if soma == n :
        return True
    else:
        return False
    
def menu():
    n = int(input('Exibir numeros pefeitos ate: '))

    for val in range(1, n+1):
        if (perfect(val)):
            print(val)

while True:
    menu()