"""import random
def selection_sort(v):
    i = 0
    while i < len(v) - 1:
        menor = i
        j = + 1
        #em busca pelo menor elemento
        while j < len(v):
            if v[i] < v[menor]:
                menor = j
            j += 1
            #verifica precisa fazer a troca
        if menor != i:
            temp = v[i]
            v[i] = v[menor]
            v[menor] = temp
        i += 1

vetor = list(range(0,10))
random.shuffle(vetor)
selection_sort(vetor)
print(vetor)"""

import random
import time

def ordenacao_selecao(A):
    n = len(A)
    # Percorre o arranjo A.
    for i in range(n):
        # Encontra o elemento mínimo em A.
        minimo = i
        for j in range(i + 1, n):
            if A[minimo] > A[j]:
                minimo = j
        # Coloca o elemento mínimo na posição correta.
        A[i], A[minimo] = A[minimo], A[i]

A = list(range(0,10000))
random.shuffle(A)
#print("Arranjo não ordenado: ", A)
antes = time.time()
ordenacao_selecao(A)
depois = time.time()
total = (depois - antes)*1000
#print("Arranjo ordenado:", A)
print("o tempo total foi: %0.2f"%total)