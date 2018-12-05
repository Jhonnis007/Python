'''
Desenvolva um programa que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaoixo de 18.5: Abaixo do Peso
- Entre 18.5e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
Fórmula: O cálculo do IMC é feito dividindo o peso (em quilogramas) pela altura (em metros) ao quadrado
'''

peso = float(input('Informe o seu peso (Kg): '))
altura = float(input('Informe a sua altura (m): '))
imc = peso / (altura ** 2)

print('O seu IMC é {:.1f} e você '.format(imc), end='')

if imc < 18.5:
    print('esta abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('esta com o peso ideal!')
elif imc >= 25 and imc < 30:
    print('esta com sobrepeso!')
elif imc >= 30 and imc <= 40:
    print('esta obeso!')
elif imc > 40:
    print('esta com obesidade mórbida!')
