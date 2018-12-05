'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
crescente.
'''


listanum = list()
while True:
    n = int(input('Digite um número: '))
    if n not in listanum:
       listanum.append(n)
       print('Registro inserido com sucesso!')
    else:
       print('Valor duplicado! Registro não inserido!')

    sn = ' '
    while sn not in 'SN':
        sn = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if sn == 'N':
       break

listanum.sort()
print(f'O valores digitados em ordem crescente foram: {listanum}')


