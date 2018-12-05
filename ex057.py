'''
 Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F.
 Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

sexo = str(input('Digite o sexo da pessoa: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos! Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrados com sucesso!'.format(sexo))
