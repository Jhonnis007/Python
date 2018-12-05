''' Escvreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em
quantos anos ele vai pagar.
A prestação não pode exceder 30% do salário ou então o empréstimo será negado.
'''

vlr_casa = float(input('Qual o valor da casa R$ '))
salario = float(input('Qual o seu salário R$ '))
anos = int(input('Em quantos anos você irá pagar? '))

prestacao = salario * 30 /100
financiamanto = vlr_casa / (anos * 12)

if financiamanto > prestacao:
    print('Financiamento NEGADO!')
else:
    print('Financiamento APROVADO')




