# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex.: Ana Maria de Souza. Primeiro: Ana Último = Souza

nome = str(input('Digite seu nome completo: ')).strip()
print('Olá, prazer em te conhecer!')
lista = nome.split()
print('Seu primeiro nome é {}'.format(lista[0]))
print('Seu ultimo nome é {}'.format(lista[len(lista)-1]))

