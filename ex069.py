'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos;
B) Quantos homens foram cadastrados;
C) Quantas mulheres tem menos de 20 anos.
'''

print('\033[31m*' * 20)
print('PROGRAMA DE CADASTRO')
print('*' * 20)
print('\033[m')

maior18 = totM = totF = 0

while True:
    idade = int(input('Informe a idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo: [M/F]')).upper().strip()[0]

        if idade > 18:
            maior18 += 1

        if sexo == 'M':
            totM += 1

        if sexo == 'F' and idade < 20:
            totF += 1

    sn = ' '
    while sn not in 'SN':
        sn = str(input('Deseja continuar? [S/N]')).upper().strip()[0]

    if sn == 'N':
        break

print(f'\n{maior18} pessoas tem mais de 18 anos.')
print(f'{totM} homens foram cadastrados no programa.')
print(f'{totF} mulheres tem menos de 20 anos.')

