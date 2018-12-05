'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120
'''

# from math import factorial

n = int(input('Digite um número para calcular o seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

'''
n = int(input('Digite um número para calcular o seu Fatorial: '))
print('Calculado o {}! = '.format(n), end='')
c = n
f = 1
for c in range(1, n + 1):
    print('{}'.format(n),end='')
    print(' x ' if c < (n + 3) else ' = ', end='')
    f *= c
    n -= 1
print('{}'.format(f))
'''

