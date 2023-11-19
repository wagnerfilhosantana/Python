def con_hora(h,m):
    if 0 < h <= 12 and 0 < m <= 60:
        print(f'{h}:{m} AM')
    elif 12 < h <= 24 and 0 < m <= 60:
        print(f'{h - 12}:{m} PM')
    else: 
        print('Valor invalido!')
def menu():
    h = int(input('Hora: '))
    m = int(input('Minutos: '))
    con_hora(h,m)

while True: 
    menu()