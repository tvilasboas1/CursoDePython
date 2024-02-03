""" Crie um programa que leia 'dois valores ' e mostre um menu na tela:

[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa

Seu programa devera realizar a operação solicitada em cada caso."""

print('Ler valores é mostrar opções na tela: ')
val1 = int(input('Informe o PRIMEIRO valor: '))
val2 = int(input('Informe o SEGUNDO valor: '))

menu = 0
while menu != 5:
    print("""\nINFORME A OPÇÃO DESEJADA P/ OS NUMEROS: 
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
    """)
    menu = int(input('Informe a opção Desejada: '))
    if menu == 1:
        print('...Então vamos SOMAR: {} + {} = {}'.format(val1, val2, val1 + val2))
    elif menu == 2:
        print('....Então vamos MULTIPLICAR: {} x {} = {} '.format(val1, val2, val1 * val2))
    elif menu == 3:
        if val1 > val2:
            print('PRIMEIRO VALOR É MAIOR.')
        elif val1 == val2:
            print('AMBOS NUMEROS SÃO IGUAIS')
        else:
            print('SEGUNDO VALOR É MAIOR.')
    elif menu == 4:
        val1 = int(input('Informe o PRIMEIRO valor: '))
        val2 = int(input('Informe o SEGUNDO valor: '))

    elif menu == 5:
        print('\nSAINDO DO PROGRAMA. OBRIGADO THIAGO hiahiahaihaihai')
    else:
        print('Opção Invalida. TENTE NOVAMENTE. ')