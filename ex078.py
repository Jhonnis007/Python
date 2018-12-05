'''Faça uim programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o
 maior e o menor valor digitado e as suas respectivas posições na lista '''

lista = list()
maior = menor = pos1 = pos2 = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um numero na posição {c}: ')))

    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        elif lista[c] < menor:
            menor = lista[c]

print(f'A lista digitada foi: {lista}')
print(f'O maior valor digitado foi o {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi o {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')




