# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

##import math

from math import hypot
c_ops = float(input('Informe o valor do cateto oposto: '))
c_adj = float(input('Informe o valor do cateto adjacente: '))
hip = hypot(c_ops,c_adj)
print('O valor da hipotenusa é: {:.2f}'.format(hip))

