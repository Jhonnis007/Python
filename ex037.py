''' Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''

import math
numero = int(input('Informe um numero inteiro: '))
print('[1 - Binário]')
print('[2 - Octal]')
print('[3 - Hexadecimal]')
base = int(input(' Escolha a base de conversão: '))

if base == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('{} opção inválida!'.format(base))





