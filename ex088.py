'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 númeors entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep
print('=-' * 20)
print('          PALPITES MEGA SENA')
print('=-' * 20)
qtde = int(input('Quantos jogos voce quer jogar? '))
print()
lista = []
jogos = []
tot = 1

while tot <= qtde:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'Sorteando {qtde} JOGOS: ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*4, '< BOA SORTE! >', '-='*4)



