'''
    Faça um programa que tenha uma função chamada contador(), que receba três parâmentros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
    A) De 1 até 10, de 1 em 1
    B) De 10 até 0, de 2 em 2
    C) Uma contagem personalizada.
'''
''' Minha solucao
from time import sleep

lista = list()

def contador(i, f, p):
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    for p in range(i, f, p):
        sleep(0.5)
        print(f'{p}', end=' ')
    print()


# Programa Principal
contador(1, 10, 1)
contador(10, 0, -2)

inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))

if passo == 0:
    passo = 1
if fim <= 0:
    passo *= -1

contador(inicio, fim, passo)

'''

from time import sleep

def contador(i, f, p):

    if p == 0:
        p = 1
    if p < 0:
        p *= -1

    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)


    if i < f:
        cont = i
        while cont <= f:
            sleep(0.3)
            print(f'{cont}', end=' ')
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            sleep(0.3)
            print(f'{cont}', end=' ')
            cont -= p
        print('FIM!')


#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar!')
ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))

contador(ini, fim, pas)



