'''
Aprimore o desafio anterior 86 (Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo
                                teclado. No final, mostre a matriz na tela, com a formatação correta.),
                                mostrando no final:
A) A soma de todos os valores pares digitados;
B) A soma dos valores da terceira coluna;
C) O maior valor da segunda linha.
'''

par = []
impar = []
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
totpar = totterceira = maiorvalor = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Digite um valor para {l, c}: ')))

        if matriz[l][c] % 2 == 0:
            par.append(matriz[l][c])
            totpar += matriz[l][c]
        elif matriz[l][c] % 2 == 1:
            impar.append(matriz[l][c])

        ''' Minha solução
        if matriz[l][2] != 0:
            totterceira += matriz[l][2]

        if matriz[1][0]:
            maiorvalor = matriz[1][0]
        if matriz[1][1] > maiorvalor:
            maiorvalor = matriz[1][1]
        if matriz[1][2] > maiorvalor:
            maiorvalor = matriz[1][2]
        '''

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'Os números pares são: {par}. ', end='')
print(f'Sua soma é {totpar}')
#print(f'Os números ímpares são: {impar}')
for l in range(0, 3):
    totterceira += matriz[l][2]
print(f'A somatória dos valores da terceira coluna é: {totterceira}')
for c in range(0, 3):
    if c == 0:
        maiorvalor = matriz[1][c]
    elif matriz[1][c] > maiorvalor:
        maiorvalor = matriz[1][c]
print(f'O maior valor da segunda linha é {maiorvalor}')





