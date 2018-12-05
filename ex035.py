# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('\033[35m' '-=' '\033[m' * 20)
print('Analisador de triângulos')
print('\033[35m' '-=' '\033[m' * 20)
r1 = float(input('Informe o valor da primeira reta: '))
r2 = float(input('Informe o valor da segunda reta: '))
r3 = float(input('Informe o valor da terceira reta: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r2 + r1):
    print('Os seguimentos digitados PODEM forma um triângulo')
else:
    print('Os seguimentos digitados NÂO podem formar um triângulo')
