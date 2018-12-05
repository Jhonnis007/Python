'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disto, vooê deve mostrar,
para cada palavra, quais são as suas vogais.
'''

palavras = ('APRENDER',
            'PROGRAMAR',
            'LINGUAGEM',
            'PYTHON',
            'CURSO',
            'GRATIS',
            'ESTUDAR',
            'PRATICAR',
            'TRABALHAR',
            'MERCADO',
            'PROGRAMADOR',
            'FUTURO')

vogais = ('A', 'E', 'I', 'O', 'U')

for p in palavras:
    print(f'\nNa palavra {p} temos as vogais ', end='')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end=' ')


