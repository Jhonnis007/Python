''' Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA

'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junta = ''.join(palavra)
#inverso = '' OU
inverso = junta[::-1]
'''
for letra in range(len(junta) -1, -1, -1):
    inverso += junta[letra]'''

print(junta, inverso)

if inverso == junta:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')




