# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n1 = float(input('Digite o valor em metros: '))
cm = n1 * 100
mm = n1 * 1000
km = n1 / 1000
dm = n1 / 10
hm = n1 / 100


print('Valor em centímetros é: {:.2f}'.format(cm))
print('Valor em milímetros é: {:.2f}'.format((mm)))
print('Valor em Kilometros é: {:.3f}'.format(km))
print('Valor em Decametros é: {:.2f}'.format(dm))
print('Valor em Hoctometro é: {:.2f}'.format(hm))


