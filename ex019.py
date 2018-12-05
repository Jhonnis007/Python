# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido.

from random import choice
n1 = str(input('Digite o nome do 1º aluno: '))
n2 = str(input('Digite o nome do 2º aluno: '))
n3 = str(input('Digite o nome do 3º aluno: '))
n4 = str(input('Digite o nome do 4º aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno que foi escolhido para apagar a lousa foi: {}'.format(escolhido))



