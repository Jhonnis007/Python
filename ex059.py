'''
Crie um programa que leia dois valores e mostre um menu como abaixo:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

from time import sleep
menu = 0
n1 = 0
n2 = 0

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

while menu != 5:
      sleep(2)
      menu = int(input(''' \n [1] SOMAR \n [2] MULTIPLICAR \n [3] MAIOR \n [4] NOVOS NÚMEROS \n [5] SAIR DO PROGRAMA \n '''))

      if menu == 1:
          soma = n1 + n2
          print('A soma entre {} + {} é {}.'.format(n1, n2, soma))
      elif menu == 2:
          multiplica = n1 * n2
          print('A multiplição de {} x {} é {}.'.format(n1, n2, multiplica))
      elif menu == 3:
          if n1 > n2:
              maior = n1
          else:
              maior = n2
          print('O númeiro maior entre {} e {} é {}'.format(n1, n2, maior))
      elif menu == 4:
          n1 = int(input('Digite um número: '))
          n2 = int(input('Digite outro número: \n'))
      else:
          if menu != 5:
            print('Função inválida! Digite novamente.')

print('Finalizando...')
sleep(2)
print('Obrigado! Volte sempre!')

