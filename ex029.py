'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada KM acima do limite.
'''

v = float(input('Qual a velocidade do carro? '))
if v > 80:
    print('Você ultrapassou a velocidade permitida e foi multado! Você terá que pagar R$ {:.2f}'.format((v - 80) * 7))
else:
    print('Você esta dentro do limite, continue dirigindo assim!')
