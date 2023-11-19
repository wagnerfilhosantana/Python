import random 
import time
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = list(range(0, 10000))
random.shuffle(alist)
antes = time.time()
vetor1 =bubbleSort(alist)
depois = time.time()
total = (depois - antes)*1000
print(total)
