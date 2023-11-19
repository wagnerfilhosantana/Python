def soma(n1, n2):
    s = n1 + n2
    return s
def subtracao(n1,n2):
    sub = n1 - n2 
    return sub
def multiplicacao(n1,n2):
    m = n1 * n2
    return m
def divisao(n1,n2):
    d = n1 / n2
    return d

n1 = int(input('Digite um numero: '))
ope = input('Digite a operacao: ')
n2 = int(input('Digite um outro numero: '))

s = soma(n1,n2)
sub = subtracao(n1,n2)
m = multiplicacao(n1,n2)
d = divisao(n1,n2)

if ope == '+':
    print(f'Resultado: {s}')
if ope == '-':
    print(f'Resultado: {sub}')
if ope == '*':
    print(f'Resultado: {m}')
if ope == '/':
    print(f'Resultado: {d}')