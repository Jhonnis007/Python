# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.

a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('So tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Esta em maiúsculo? ', a.isupper())
print('Esta em minúsculo? ', a.islower())
print('Esta em capitalizada? ', a.istitle())
