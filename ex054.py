'''
  Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores.
'''

from datetime import date
dt_atual = date.today().year
menores = 0
maiores = 0

for c in range(1,8):
    ano = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    idade = dt_atual - ano

    if idade <= 21:
        menores += 1
    else:
        maiores += 1
print('\nAo todo tivemos {} pessoas maiores de idade'.format(maiores))
print('E também tivemos {} pessoas menores de idade.'.format(menores))

