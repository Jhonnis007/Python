'''
Crie um programa onde o usuário possa digitar cinco valores numériocos e cadastre-os em uma lista, já na posição
correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

maior = menor = 0
lista = list()
for v in range(0, 5):
    num = int(input(f'Digite o {v+1}º valor: '))

    if v == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionando na posição {pos} da lista...')
                break
            pos += 1

print(f'Os valores digitados em ordem foram {lista}')




