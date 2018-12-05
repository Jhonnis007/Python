'''
Faça um programa que leia nome e peso, de várias pessoas, guardando tudo em uma lista. No final mostre:
A) Quantas pessoas foram cadastradas;
B) Uma listagem com as pessoas mais pesadas;
C) Uma listagem com as pessoas mais leves.
'''

temp = []
princ = []
maior_peso = menor_peso = 0

while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peso: ')))

    if len(princ) == 0:
        maior_peso = menor_peso = temp[1]
    else:
        if temp[1] > maior_peso:
            maior_peso = temp[1]
        if temp[1] < menor_peso:
            menor_peso = temp[1]
    princ.append(temp[:])
    temp.clear()

    sn = ' '
    while sn not in 'SN':
        sn = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if sn == 'N':
        break

print(f'Foram cadastradas {len(princ)} pessoas.')
print(f'O maior peso é de {maior_peso}Kg. E é do ', end='')
for p in princ:
    if p[1] == maior_peso:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso é de {menor_peso}Kg. E é do ', end='')
for p in princ:
    if p[1] == menor_peso:
        print(f'[{p[0]}]', end=' ')


