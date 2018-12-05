'''
Faça um programa que leia nome e média de uma aluno, guardando também a situação em um diciário. No final, mostre
o conteúdo da entrutura
=> 7 aprovado menor Reprovado
'''

aluno = {'Nome': str(input('Nome do Aluno: ')),
         'Media': float(input('Média: '))}
if aluno['Media'] >= 7:
    situacao = 'APROVADO'
else:
    situacao = 'REPROVADO'
aluno['Situação'] = situacao

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
