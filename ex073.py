'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre:

A) OS 5 primeiros;
B) Os últimos 4 colocados;
C) Times em ordem alfabéticas;
D) Em que posição está o time da Chapeciense.
'''

times = ('São Paulo', 'Internacional', 'Palmeiras', 'Flamengo', 'Grêmio', 'Atlético', 'Cruzeiro',
         'Corinthians', 'Santos', 'Fluminense', 'Atlético-PR', 'América-MG', 'EC Vitória', 'Bahia',
         'Botafogo', 'Chapecoense', 'Ceará SC', 'Vasco da Gama', 'Sport Recife', 'Paraná')

print(f'Os cinco primeiros times são: {times[0:5]}')
print(f'Os últimos quatro colocados são: {times[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(times)}')
print(f'O time da Chapecoense esta na {times.index("Chapecoense") +1}ª posicao.')


