'''
Faça um programa que joge par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele consquistou no final do jogo.
'''
from random import randint
print('~' * 21)
print(' \033[34m JOGO PAR OU ÍMPAR \33[m')
print('~' * 21)
r = cont = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('PAR ou ÍMPAR: [P/I]')).upper().strip()[0]

    r = jogador + computador
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {r}. ', end='')
    print('DEU PAR' if r % 2 == 0 else 'DEU ÍMPAR')
    if escolha == 'P' and r % 2 == 0:
        vencedor = 'JOGADOR'
        cont += 1
    elif escolha == 'I' and r % 2 == 1:
        vencedor = 'JOGADOR'
        cont += 1
    else:
        vencedor = 'COMPUTADOR'
    print(f'O vencedor foi o {vencedor}!')

    if vencedor == 'COMPUTADOR':
        break

print(f'\033[31m GAME OVER!!! \033[m Você venceu {cont} vezes!')
