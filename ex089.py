'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
mostre um boletim contendo a média de cada um e permita que o usuário possa mostra as notas de cada aluno
individualmente.

Minha solução:

temp = []
lista = []
media = 0
print('-='*4, 'PROGRAMA NOTAS DE ALUNOS', '-='*4)
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))

    media = (nota1 + nota2) / 2
    temp.append(nome)
    temp.append(nota1)
    temp.append(nota2)
    temp.append(media)
    lista.append(temp[:])
    temp.clear()
    sn = ' '
    while sn not in 'SN':
        sn = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
    if sn == 'N':
        break
print('=-' * 30)
print('Nº  NOME        MÉDIA')
print('-'*20)
for i, l in enumerate(lista):
    print(f'{i} {lista[i][0]:^10} {lista[i][3]:^10}')
print('-'*30)
aluno = 0
while aluno != 999:
    aluno = int(input('Deseja mostrar as notas de qual aluno? (999 interromper)'))
    print(f'As notas de {lista[aluno][0]} são: {lista[aluno][1], lista[aluno][2]}')
    if aluno == 999:
        break
print('-='*5, 'FIM DO PROGRAMA', '-='*5)

GUANABARA:
'''

print('-='*10, 'FICHA DE ALUNOS', '-='*10 )
ficha = list()
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    sn = ' '
    while sn not in 'SN':
        sn = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if sn == 'N':
        break
print('-='*30)
print(f'{"Nº":<4} {"NOME":<10} {"MÉDIA":>8}')
print('-='*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostrar as notas de qual aluno? (999-Interromper): '))
    if opc == 999:
        print('FINALIZANDO...')
        break

    if opc <= len(ficha) - 1:
        print(f'As notas de {ficha[opc][0]} são: {ficha[opc][1]}')
print('VOLTE SEMPRE!')































