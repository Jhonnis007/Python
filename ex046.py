# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
from emoji import emojize
for contagem in range(10, -1, -1):
    sleep(1)
    print(contagem)
print('BOM BOM BOMMMM!', end=' ')
print(emojize(':tada:', use_aliases = True))

