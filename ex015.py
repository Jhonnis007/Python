# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Kn rodado.

km = float(input('Informe a quantidade de Kms percorridos: '))
dias = int(input('Informe a quantidade de dias alugados: '))
preco = dias * 60 + 0.15 * km
print('O preço a ser pago por {:.0f} Km rodados durante {} dias de aluguel é de R$ {:.2f}'.format(km, dias, preco))
