'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1 + n2) / 2

print('Tirando nota {:.1f} e nota {:.1f}, a média é: {:.1f}'.format(n1, n2, media))

if media < 5:
    print('Você esta\033[31m REPROVADO! \033[m'.format(media))
elif media >= 5 and media <= 6.9:
    print('Você esta em \033[33mRECUPERAÇÃO! \033[m')
else: print('Você foi\033[32m APROVADO! \033[m')



