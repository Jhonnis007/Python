'''
    Faça uma programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
entre todos os valores PARES sorteados pela função anterior.
'''

from random import randint

numeros = list()

def sorteia():
    for c in range(0, 5):
        numeros.append(randint(1, 10))

    print(f'Foram sorteados os números {numeros}')

def somaPar(num):
    par = 0
    for valores in num:
        if valores % 2 == 0:
            par += valores

    print(f'A soma de todos os valores pares é {par}')

#Programa Principal
sorteia()
somaPar(numeros)

