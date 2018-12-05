# Crie um programa que leia um número ReaL qualquer pelo teclado e mostre na tela a sua porção inteira.
'''
import math
num = float(input('Digite um numero: '))
num_int = math.trunc(num)
print('O numero {} tem a parte Inteira igual a {}'.format(num, num_int))
'''
'''
from math import trunc
num = float(input('Digite um numero: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))

