# Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint
print('{:=^40}'.format(' JOKENPÔ '))
lista = ['PEDRA', 'PAPEL', 'TESOURA']
print('''
[ 0 ] PEDRA
[ 1 ] PEPEL
[ 2 ] TESOURA
''')

jogador = int(input('Escolha sua opção: '))
computador = randint(0,2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('')

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('O JOGADOR VENCEU!')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU!')
    else:
        print('Jogada inválida')

elif computador == 1:
    if jogador == 0:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('O JOGADOR VENCEU!')
    else:
        print('Jogada inválida')

elif computador == 2:
    if jogador == 0:
        print('O JOGADOR VENCEU!')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida')

print('O computador jogou {}'.format(lista[computador]))
print('O jogador jogou {}'.format(lista[jogador]))

