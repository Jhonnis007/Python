'''
Escreva um programa que leia dois número inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- o segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número {} é o maior'.format(n1))
elif n2 > n1:
    print('O segundo número {} é o maior'.format(n2))
else:
    print('Não existem valores maiores, os dois são iguais: {} e {}'.format(n1, n2))



