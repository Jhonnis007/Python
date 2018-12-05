'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000,00
C) Qual é o nome do produto mais barato.
'''

print('\033[31m=-' * 10)
print('   LOJAS BARATÃO')
print('=-' * 10)
print('\033[m')

totgasto = cont = contmaior = totmenor = 0
nbarato = ' '

while True:
    nomeprod = str(input('Digite o nome do produto: ')).upper().strip()
    precoprd = float(input('Digite valor do produto: R$ '))

    totgasto += precoprd
    cont += 1

    if precoprd >= 1000:
        contmaior += 1

    if cont == 1 or precoprd < totmenor:
        totmenor = precoprd
        nbarato = nomeprod

    sn = ' '
    while sn not in 'SN':
        sn = str(input('Deseja continuar digitando os produtos? [S/N]')).upper().strip()[0]

    if sn == 'N':
        break

print(f'O total da compra foi R$ {totgasto:.2f}')
print(f'{contmaior} produtos custaram mais de R$ 1000,00')
print(f'O produto mais barato foi {nbarato} por R$ {totmenor:.2f}')
print('{:-^40}'.format(' FIM DO PROGRAMA '))