'''
  Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
  Sequencia de Fibonacci
  Ex.: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''

print('-' * 25)
print('SEQUÊNCIA DE FOBONACCI')
print('-' * 25)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
t3 = 0
c = 3 # Começa no 3 porque eu já mostrei o 1 o 2
print('{} -> {}'.format(t1, t2), end=' -> ')
while c <= n:
    t3 = t1 + t2
    print('{}'.format(t3), end=' -> ')
    t1 = t2
    t2 = t3
    c += 1
print('FIM')
