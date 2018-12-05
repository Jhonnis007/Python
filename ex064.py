'''
Crie um programa que leia vários número inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos
números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
'''

soma = numero = cont = 0
numero = int(input('Digite um numero para se somado ou 999 para parar: ')) # 'GAMBIARRA' para nao ler o 999
while numero != 999:
      soma += numero
      cont += 1
      numero = int(input('Digite um numero para se somado ou 999 para parar: '))
print('A soma dos {} valores digitados foi: {}'.format(cont, soma))

