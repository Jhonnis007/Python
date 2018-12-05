'''
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas lista extras que vão
contar apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
três listas geradas.
'''

numeros = list()
impar = list()
par = list()
while True:
    numeros.append(int(input('Digite um número:')))
    sn = ' '
    while sn not in 'SN':
        sn = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if sn == 'N':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
       par.append(v)
    else:
       impar.append(v)

print(f'A lista digitada foi {numeros}')
print(f'A lista de números pares é {par}')
print(f'A lista de númeors ímpares é {impar}')

