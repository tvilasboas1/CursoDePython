"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

A vista dinheiro / Cheque: 10% de dsconto
A vista no cartão: 5% desconto
em ate 2x no cartao: preço normal
3x ou mais no cartão: 20% de juros"""

print('-'*25)
prod = float (input('Informe o valor do produto: '))
print('-'*25)
print("""CONDIÇÕES DE PAGAMENTO
[1] A VISTA / DINHEIRO 
[2] A VISTA / CARTAO DEBITO
[3] ATE 2X NO CARTAO
[4] ACIMA DE 3X NO CARTAO""")
print('-'*25)
cond = int(input('Informe o codigo da condição: '))
print('-'*25)

if cond == 1:
    print('Venda a Vista C/Dinheiro,  DESC 10%TOTAL: ', prod - (prod * 10/100) )
elif cond == 2:
    print ('Venda a Vista C/ Cartão DESC 5% TOTAL: ', prod - (prod * 5 /100))
elif cond == 3:
    print('Venda em ate 2x no Cartão: ', prod)
elif cond ==4:
    print('Venda 3x / 10x no Cartão: JUROS10% ', prod + (prod * 10/100))
else:
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE.')
