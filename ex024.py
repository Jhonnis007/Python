# Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome 'SANTO'

cidade = str(input('Digite o nome da cidade: ')).strip()
cidade = cidade.upper()
print(cidade.startswith('SANTO'))
# print(cidade[:5].upper() == 'SANTO')

