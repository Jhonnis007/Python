'''
Refaça o Desafio 035 dos triângulos, acrescetando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: doios lados iguais
- Escaleno: todos os lados diferentes
'''

r1 = float(input('Digite o primeiro segmento da reta: '))
r2 = float(input('Digitel o segundo segmento da reta: '))
r3 = float(input('Digite o terceiro segmento da reta: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r2 + r1):
    print('As retas {}, {} e {} formam um triângulo'.format(r1, r2, r3), end=' ')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('As retas acima NÂO podem formar um triângulo!')




