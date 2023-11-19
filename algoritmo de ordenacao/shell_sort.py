import random
import time

def shell_sort(vetor):
    h = len(vetor)//2
    while h > 0:
        i = h
        for i in range(h, len(vetor)):
            temp = vetor[i]
            j = i
            while j >= h and vetor[j - h] > temp:
                vetor[j] = vetor[j - h]
                j -= h
            vetor[j] = temp
        h = h // 2
    return vetor

lista = list(range(0,1000000))
random.shuffle(lista)
antes = time.time()
shell_sort(lista)
depois = time.time()
total = (depois - antes)*1000
#print(lista) 
print("o tempo total e %0.2f"%total)
