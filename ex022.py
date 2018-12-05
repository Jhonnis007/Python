''' Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as leatras maiúsculos e minúsculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome
'''

nome = str(input('Digite um nome: ')).strip()
print('O nome em maiúsculo é: {}'.format(nome.upper()))
print('O nome em minúsculo é: {}'.format(nome.lower()))
print('A quantidade de letras é: {}'.format(len(nome) - nome.count(' ')))
#print('O primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
