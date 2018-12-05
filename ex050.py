''' Desenvolva um programa que leia seis número inteiros e mostre a soma apenas
daqueles que forem pares. Se o vlaor digitado for impar, desconsidere-o'''

soma = 0
cont = 0
for c in range(1,7):
    numero = int(input('Digite o {}º numero inteiro: '.format(c)))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print('A soma dos {} numeros pares digitados é {}'.format(cont, soma))


