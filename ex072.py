'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

numeros = ('ZERO', 'UM', 'DOIS', 'TRES', 'QUATRO', 'CINCO',
           'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE',
           'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESEIS',
           'DEZESETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

while True:

    while True:
        num = int(input('Digite um número inteiro entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')

    print(f'Você digitou o número {numeros[num]}')

    continua = str(input('Deseja continuar? [S/N]')).upper().strip()[0]

    if continua == 'N':
        break

print('FIM DO PROGRAMA')





