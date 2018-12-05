'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
# maior = menor = num[0]
print(f'A lista gerada foi: ', end='')
for n in num:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(num)}') # Solução Guanabara
print(f'O menor valor sorteado foi {min(num)}') # Solução Guanabara


''' MINHA SOLUÇÃO
for c in range(0, len(num)):
    if num[c] > maior:
        maior = num[c]
    elif num[c] < menor:
        menor = num[c]
print(f'O número maior é: {maior}')
print(f'O número menor é: {menor}')
'''



