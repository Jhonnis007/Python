# Escreva um programa que pergunte o salário de um fundionário e calculo o valor do seu aumento.
# Para salário superiores a R$ 1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe o valor do salário R$: '))

if salario >= 1250:
    novo_salario = salario + (salario * 10 /100)
else:
    novo_salario = salario + (salario * 15 /100)
print('O salário de \033[31m R${:.2f} \033[m com o aumento, passa a ser de \033[32m R${:.2f} \033[m'.format(salario, novo_salario))


