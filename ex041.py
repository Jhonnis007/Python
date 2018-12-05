'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIN
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
'''

from datetime import date
nascimento = int(input('Informe o ano de seu nascimento: '))
dt_atual = date.today().year
idade = dt_atual - nascimento

if idade <= 9:
    print('Para idade de {} anos, a categoria é a {}.'.format(idade, 'MIRIM'))
elif idade <= 14:
    print('Para idade de {} anos, a categoria é a {}.'.format(idade, 'INFANTIL'))
elif idade <= 19:
    print('Para idade de {} anos, a categoria é a {}.'.format(idade, 'JUNIOR'))
elif idade <= 25:
    print('Para idade de {} anos, a categoria é a {}.'.format(idade, 'SÊNIOR'))
elif idade > 25:
    print('Para idade acima de {} anos, a categoria é a{}.'.format(idade, 'MASTER'))


