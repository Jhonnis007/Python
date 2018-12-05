'''
Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o
salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import date
dados = dict()
dados['nome'] = str(input('Digite o nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['CTPS'] == 0:
    for k, v in dados.items():
        print(f' - {k} tem o valor {v}')
else:
    dados['contratação'] = int(input('Informe o ano da contratação: '))
    dados['salário'] = float(input('Informe o salário: R$ '))
    dt_apos = dados['idade'] + (35 - (date.today().year - dados['contratação']))
    dados['aposentadoria'] = dt_apos
    print('-=' * 30)

    for k, v in dados.items():
        print(f' - {k} tem o valor {v}')

