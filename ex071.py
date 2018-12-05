'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuãrio qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs.: Considere que o caixa possui cédulas de R$ 50,00, R$ 20,00, R$ 10,00 e R$ 1,00
'''

print('=' * 30)
print('{:^30}'.format('CAIXA ELETRÔNICO '))
print('=' * 30)

valor = int(input('Qual o valor a ser sacado? R$ '))
total = valor
céd = 50
totcéd = 0

while True:

    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R$ {céd:.2f}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0

        if total == 0:
            break

print('SAQUE CONCLUÍDO')

