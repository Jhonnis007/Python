# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

#ano = int(input('Informe o ano: '))

from datetime import date
ano = int(input('Informe o ano ou coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year  #pega o ano atual

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    result = str('ANO BISSEXTO')
else:
    result = str('ANO NAO É BISSEXTO')
print('O ano {} {}'.format(ano, result))
