# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input('Informe o salario do funcionario: R$ '))
novo_sal = salario + (salario * 15 / 100)
print('O novo salario do funcionário com 15% de aumento é R$ {:.2f}'.format(novo_sal))

