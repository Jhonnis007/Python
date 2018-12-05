'''
    Crie um programa que leia nome, sexo, e idade de várias pessoas, guardando os dados de cada pessoa em um
dicionário e todos os dicionários em uma lista. No final, mostre:

    A) Quantas pessoas cadastradas;
    B) A média de idade;
    C) Uma lista com mulheres;
    D) Uma lista com idade acima da média.

'''

pessoas = dict()
galera = list()
soma = media = 0

while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: '))
    while True:
        pessoas['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoas['Sexo'] in ('MF'):
            break
        print('ERRO! Digite M/F')
    pessoas['Idade'] = int(input('Idade: '))
    soma += pessoas['Idade']
    galera.append(pessoas.copy())
    while True:
        sn = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        if sn in ('SN'):
            break
        print('ERRO! Digite apenas S ou N.')
    if sn == 'N':
        break
print('-=' * 30)
print(galera)
print(f'A quantidade de pessoas cadastradas é {len(galera)}')
media = soma / len(galera)
print(f'A média das idades é {media:5.2f}')
print('As mulheres cadastradas são: ', end='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end='')
print()
print('As pessoas com a idade acima da média: ', end='')
for p in galera:
    if p['Idade'] >= media:
        print(f'{p["Nome"]} ', end='')
print()






