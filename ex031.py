# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por KM para
# viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Informe a distancia a ser percorrida: '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('Voce irá percorrer {}Km, e sua passagem será de R${:.2f}.'.format(distancia, preco))

'''
if distancia <= 200:
    print('Esta viagem de \033[34m {}Km \033[m é mais curta e você pagará R$ {:.2f} na passagem!'.format(distancia, distancia * 0.50))
else:
    print('Esta viagem de \033[34m {}Km \033[m é mais longa e você pagará R$ {:.2f} na passagem!'.format(distancia, distancia * 0.45))
'''

