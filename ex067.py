'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''

print('====== PROGRAMA DE TABUADAS ======')
while True:
    tab = int(input('Qual a tabuada você quer ver? '))
    if tab < 0:
        break
    for c in range(1, 11):
        print(f'{tab} x {c} = {tab * c}')
print('Fim do programa TABUADAS')
