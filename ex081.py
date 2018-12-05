'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados;
B) A lista de valores, ordenada de forma decrescente;
C) Se o valor 5 foi digitado e está ou não na lista.
'''

cont = 0
lista = []
while True:
    lista.append(int(input('Digite um numero: ')))
    sn = ' '
    while sn not in 'SN':
        sn = str(input('Deseja continuar? [S/N]')).upper().strip()[0]

    lista.sort(reverse=True)

    if sn == 'N':
        break

print(f'Foram digitados {len(lista)} números')
print(f'A lista ordenada de forma decrescente é {lista}')
if 5 in lista:
    print(f'O número 5 esta na lista na posição {lista.index(5)}')
else:
    print(f'O número 5 não esta lista.')







