'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores.
'''

continua = True
soma = media = cont = maior = menor = 0
opcao = ''
while continua == True:
    numero = int(input('Digite um número: '))
    cont += 1
    soma += numero

    if cont == 1: # Não esquecer este flag
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

    opcao = str(input('Deseja continuar [S/N]: ').upper()).strip()[0] # Consideta só a primeira letra

    if opcao == 'N':
        continua = False

media = soma / cont
print('A média dos {} valores digitados é {}'.format(cont, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))











