def somaimposto(p):
    if p >= 1 and p <= 100:
        imp = 1.03 * p
    elif p > 101:
        imp = 1.12 * p
      
    return imp

def menu():

    p = float(input('Digite o valor do produto para saber o imposto: '))
    imp = somaimposto(p)
    print(f'O imposto obtido do produto e: {imp:.2f}')

while True:
    menu()