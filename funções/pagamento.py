
def pagamento(p, a):
    
    return p*1.03 + a*0.001

c = t = 0

while True:
    p = float(input('Pretascao: '))
    a = int(input('Dias de atraso: '))
    res = pagamento(p,a)
    if a > 0:
        print('-+-'*10)
        print(f' O valor a ser pago: {res:.2f}')
        print('-+-'*10)
    elif a == 0:
        print('Nenhum juro a ser pago.')
    c += 1
    t += res
