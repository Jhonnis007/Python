# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode
# comprar.
# Considere U$$ 1,00 = R$ 3,27

real = float(input('Quando em dinheiro voce tem na carteira? R$'))
dolar = real / 3.27
print('Com R$ {:.2f} Voce pode comprar U$$ {:.2f}'.format(real,dolar))


