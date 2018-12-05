''' Escreca um programa que faça o computador ´pensar´ em um número inteiro entre 0 e 5 e peça o usuário
tentar descobrir qual foi o número encolhido pelo computador. O programa deverá escrever na tela se o
usuário venceu ou perdeu.
'''

from random import randint
from time import sleep

print(('-=-' * 5) + (' PENSANDO EM UM NUMERO ') + '-=-' * 5)
n = randint(0, 5)
num = int(input('Digite um numero: '))
print('PROCESSANDO...')
sleep(3)
if num == n:
    print('Parabéns, voce acertou!')
else:
    print('Que pena, voce errou! Eu pensei no número {} e voce no numero {}.'.format(n,num))


