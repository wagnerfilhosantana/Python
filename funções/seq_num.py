def seq_num(n):
    if isinstance(n, int):
        x = 1
        while x <= n :
            y = 1
            text = ''
            while y <= x:
                text += str(y) + ' '
                y += 1
            print(text)
            x += 1

def menu():
    n = int(input('Digite um numero: '))
    seq_num(n)

while True:
    menu()