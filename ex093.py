'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quatidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

nome = str(input('Nome do Jogador: '))
qtde_par = int(input(f'Quantas partidas {nome} jogou? '))
tot_gols = qtde_gols = 0
gols = list()
partidas = list()
aproveitamento = dict()

for i in range(0, qtde_par):

    qtde_gols = (int(input(f'Quantos gols na partida {i}? ')))
    tot_gols += qtde_gols
    gols.append(qtde_gols)

    aproveitamento['nome'] = nome
    aproveitamento['gols'] = gols
    aproveitamento['total'] = tot_gols
    partidas = aproveitamento['gols']
print('-=' * 30)
print(aproveitamento)
print('-=' * 30)
for k, v in aproveitamento.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {nome} jogou {qtde_par} partidas.')

for k, i in enumerate(partidas):
    print(f'=> Na partida {k}, fez {i} gols.')
print(f'Foi um total de {tot_gols} gols')












