'''
Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura While
'''

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' -> ')
    termo += razao
    cont += 1
print('FIM')