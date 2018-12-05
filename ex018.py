# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do Seno, Cosseno e Tangente desse ângulo
'''
import math
a = int(input('Digite o ângulo: '))
print('O Seno é {:.2f}, o Cosseno é {:.2f} e a Tangente é {:.2f}'.format(math.sin(math.radians(a)), math.cos(math.radians(a)), math.tan(math.radians(a))))
'''

from math import radians, sin, cos, tan
a = int(input('Digite o ângulo: '))
print('O Seno é {:.2f}, o Cosseno é {:.2f} e a Tangente é {:.2f}'.format(sin(radians(a)), cos(radians(a)), tan(radians(a))))