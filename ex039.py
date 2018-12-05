'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora de se alista ou se já passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passsou do prazo.
'''

from datetime import date
dt_nascto = int(input('Informe o ano do seu nascimento: '))
sexo = str(input('Informe o seu sexo: '))
dt_atual = date.today().year
idade = dt_atual - dt_nascto

if sexo == 'Feminino':
    print('Voce é mulher e não presica se alistar! Tenna um bom dia!')
elif idade < 18:
    print('Voce ainda tem {} anos, e seu alistamento será daqui a {} anos.'.format(idade, 18 - idade))
elif idade == 18:
    print('Você já tem {} anos, se deverá se alistar ainda este ano!'.format(idade))
else:
    print('Você ja tem {} anos, e deveria ter se alistado a {} anos atrás'.format(idade, idade - 18))
