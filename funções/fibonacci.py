#complexidade de O(2^n)
def fib(n):
    if n == 1:
        return 0
    elif n == 2: 
        return 1
    else:
        return fib(n-1) + fib(n-2)
    


#complexidade de O(n)
def fibo(n1):
    i = 0
    j = 1

    for k in range(1,n1):
        t = i + j
        i = j
        j = t
    return i 

#complexidade de O(log(n))
def fibon(n2):
    if n2 <= 0:
        return 0
    i = n2 - 1
    a = 1;b = 0;c = 0;d = 1;aux1 = 0;aux = 0
    while i > 0:
        if i%2 != 0:
            aux1 = d*b + a*c
            aux2 = d(b+a) + b*c
            a = aux1
            b = aux2
        aux1 = c**2 + d**2
        aux2 = d(2*c + d)
        c = aux1
        d = aux2
        i = i/2
    return a+b


def menu():
    n2 = int(input('Digite um numero: '))

    for val in range(1,n2+1):
        print(fibo(val))

while True:
    menu()