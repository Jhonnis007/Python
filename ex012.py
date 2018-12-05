# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: R$ '))
prc_dec = preco - (preco * 0.05)
print('O produto com o preço de R$ {:.2f}, sairá com o desconto de 5% por R$ {:.2f}'.format(preco, prc_dec))

