'''
    Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
'''

def area(l, c):
    a = l * c
    print(f'A área do terreno de {l} x {c} é de {a}M²')


#Programa Principal
print(' Controle de Terrenos ')
print('-' * 25)
l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
area(l, c)
