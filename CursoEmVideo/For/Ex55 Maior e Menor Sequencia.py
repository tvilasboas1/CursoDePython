""" Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos. """
print('--'*14)
print('ANALISE DE PESO DAS PESSOAS')
print('--'*14)
maiorPeso = 0
menorPeso = 0
cont = 0
for c in range(1,6):
    peso = float(input('Informe o Peso. {}º Pessoa: ' .format(c)))
    if c == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maior = peso
        if peso < menorPeso:
            menorPeso = peso

    cont = cont + 1
print('\nFoi feito a pesagem de {} PESSOAS.'.format(cont))
print('O maior peso lido foi: ',maiorPeso)
print('O menor peso lido foi',menorPeso)
