# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF. Formula: F=1,8C+32

c = float(input('Digite a temperatura em ºC '))
f = 1.8 * c + 32
print('A temperatura de {} ºC em ºF é {}'.format(c, f))

