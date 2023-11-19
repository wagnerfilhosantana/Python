import random
import time
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave

# Exemplo de uso
lista = list(range(0,10000))
random.shuffle(lista)
antes = time.time()
insertion_sort(lista)
depois = time.time()
total = (depois - antes)*1000
#print(lista) 
print("o tempo total e %0.2f"%total)