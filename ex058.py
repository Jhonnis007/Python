'''
Melhore o jogo do Desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador
vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

from random import randint
computador = randint(0,10)

print('Olá, eu sou o seu computador!!! E já pensei em numero entre 0 e 10.')
print('Tente adivinhar qual número eu pensei...')

acertou = False
conta = 0
jogador = int(input('\nEai, qual foi o número que eu pensei? '))
while not acertou:
    conta += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            jogador = int(input('Ainda não, tente novamente! Eu pensei em um número menor: '))
        else:
            jogador = int(input('Ainda não, tente novamente! Eu pensei em um número maior: '))
print('Parabéns!!! Em {} tentativas você acertou o numero que eu pessei: {}'.format(conta, computador))
