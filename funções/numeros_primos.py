#include <stdio.h>
#include <conio.h>
"""int main()
{
    int num, tot = 0, i = 0;
    printf("Digite um numero: ");
    scanf("%d", &num);
    for (i = 1; i <= num; i++){
        if(num % i == 0){
            tot += 1;
        }
    }
    printf("Acabou!");
    printf("\n O numero %d e divisivel por %d numeros.", num, tot);
    if (tot == 2){
        printf("O numero %d e primo.", num);
    }
    else{
        printf("O numero %d nao e primo", num);
    }
    return 0;
}"""

import os

def numerosPrimos(num):
    i = 1
    tot = 0
    while i <= num:
        if num % i == 0:
            tot += 1
        i += 1
    print(f'O numero {num} e divisivel por {tot} numeros')
    Espace()
    if tot == 2:
        print('O numero {0} e primo!' .format(num))
        Espace()
    else:
        print('O numero {0} nao primo!' .format(num))
        Espace()

def Espace():
    print('-'*50)

def Menu():
    num = int(input('digite um numero: '))
    os.system('cls')
    numerosPrimos(num) 
    
while True:
    Menu()
    finish = input('Deseja continuar, s ou n? ')

    if finish == 's' or finish == 'S':
        continue
    elif finish == 'n' or finish == 'N':
        break
    else:
        print('Valor nao reconhecido, por favor digite s ou n.')