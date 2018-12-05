'''
    Faça um programa que tenha uma função chamada maior(), que receba vários parâmentros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''


print('Analisando os parametros...')
print()
def maior(* num):

    print(f'Os paramentros passados foram {num}, total de {len(num)} e o maior número é: ', end=' ')

    mai = 0
    for m in num:

        if mai == 0:
            mai = m
        elif m > mai:
            mai = m
    print(f'{mai}')


#Programa Principal
maior(19, 4,6,43,6,3)
maior(9,6,8,4,3,65,8,2,1,8,6)
maior(6)
maior()



