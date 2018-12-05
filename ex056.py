'''
 Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
 - A média de idade do grupo
 - Qual é o nome do homem mais velho
 - Quantas mulheres tem menos de 20 anos
'''

totidade = 0
maioridade = 0
idademulher = 0
nomehomem = ''

for c in range(1, 5):

    print('===== {}ª pessoa ====='.format(c))

    idade = int(input('Qual a sua idade? ').upper())
    nome = str(input('Qual o seu nome? ').upper().strip())
    sexo = str(input('Qual o seu sexo (M/F)? ').upper())

    totidade += idade

    if c == 1 and sexo == 'M':
        maioridade = idade
        nomehomem = nome
    else:
        if idade > maioridade and sexo == 'M':
            maioridade = idade
            nomehomem = nome

    if sexo == 'F' and idade < 20:
        idademulher += 1

idademedia = totidade / 4

print('\nA média de idade do grupo é de {:.2f} anos'.format(idademedia))
if nomehomem == '':
    print('Nao existem homens nessa lista!')
else:
    print('O nome do homem mais velho é {} e tem {} anos'.format(nomehomem, maioridade))
print('{} mulher tem menos de 20 anos.'.format(idademulher))




