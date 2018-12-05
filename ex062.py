'''
Melhore o Desafio 061, perguntando para o usúario se ele quer mostrar mais alguns termos. O programa encerra
quando ele disser que quer mostrar 0 termos.
'''

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSE')
    mais = int(input('Quantos termos voce quer mostrar a mais?'))
print('\nProgressão finalizada com {} termos mostrados.'.format(total))



