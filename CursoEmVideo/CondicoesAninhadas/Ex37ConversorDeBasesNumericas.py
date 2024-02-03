"""Escreva um progama que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversao:

1 para binario
2 para octal
3 para hexadecimal"""

num = int (input ('Digite um numero inteiro: '))
print( ''' Escolha uma das bases para conversão: 
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))
if opcao == 1:
    print ('{} convertido para BINARIO é igual a {}'.format(num, bin(num))) # O python já possui conversores para Binario
elif opcao == 2:
    print ('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {} '.format(num,hex(num)))
else:
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE')
