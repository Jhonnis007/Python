''' Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se
encontram no intervalo de 1 até 500. '''

soma = 0
conta = 0
for count in range(1, 501, 2):
    if count % 3 == 0:
        conta += 1
        soma += count
print('A soma de todos os valores {} solicitados é {}'.format(conta, soma))
