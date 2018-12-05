'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

vlr_compra = float(input('Informe o valor total dos produtos R$ '))
condicao = int(input(''' Informe a condição de pagamento: 
[ 1 ] À Vista Dinheiro/Cheque
[ 2 ] À Vista Cartão
[ 3 ] 2x Cartão
[ 4 ] 3x ou mais Cartão '''))

if condicao == 1:
    vlr_final = vlr_compra - (vlr_compra * 10 /100)
    vlr_desconto = vlr_compra - vlr_final
    print('Para o pagamento à vista no dinheiro, o valor da compra de R$ {:.2f}, sairá com 10% de desconto por R$ {:.2f}'.format(vlr_compra, vlr_final))
    print('Valor total do desconto R$ {:.2f}'.format(vlr_desconto))
elif condicao == 2:
    vlr_final = vlr_compra - (vlr_compra * 5 /100)
    vlr_desconto = vlr_compra - vlr_final
    print('Para o pagamento à vista no cartão, o valor da compra de R$ {:.2f}, sairá com 5% de desconto por R$ {:.2f}'.format(vlr_compra, vlr_final))
    print('Valor total do desconto R$ {:.2f}'.format(vlr_desconto))
elif condicao == 3:
    vlr_final = vlr_compra
    print('Para o pagamento em até 2x no cartão, o valor total será de R$ {:.2f}'.format(vlr_final))
elif condicao == 4:
    prestacao = int(input('Informe a quantidade de vezes: '))
    vlr_final = vlr_compra + (vlr_compra * 20 / 100)
    vlr_acrescimo = vlr_final - vlr_compra
    print('Para o pagamento em {} vezes, o valor da compra de R$ {:.2f}, sairá com acrescimo de 20% por R$ {:.2f}'.format(prestacao, vlr_compra, vlr_final))
    print('Total total de acréscimo R$ {:.2f}'.format(vlr_acrescimo))
else:
    print('Condição Invalida!')




