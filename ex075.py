'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9;
B) Em que posição foi digitado o primeiro valor 3;
C) Quais foram os números pares
'''

num = (int(input('Digite o primeiro valor: ')),
       int(input('Digite o segundo valor: ')),
       int(input('Digite o terceiro valor: ')),
       int(input('Digite o quarto valor: ')))

print(f'Os números digitados foram {num}')
print(f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro valor 3 foi digitado na {num.index(3) +1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
#print('Os valores pares digitador foram: ', end='')
for c in num:
    if c % 2 == 0:
        print(f'O número {c} é par')
        #print(c, end=', ')





