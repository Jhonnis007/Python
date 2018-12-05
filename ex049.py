# Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

n = int(input('Informe um número para ver a sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {:2}'.format(n, c, (c * n)))



