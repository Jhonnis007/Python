# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR

#import math
numero = int(input('\033[35m Digite um numero inteiro: ' '\033[m'))

if numero % 2 == 0:
   print('O numero {} é um número PAR'.format(numero))
else:
    print('O numero {} é um número IMPAR'.format(numero))