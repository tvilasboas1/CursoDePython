"""" Crie um programa que leia o nome e o preço de varios produtos. O programa devera perguntar se o usuario vai continuar. No final mostre:

A) Qual é o total de gasto na compra ?
B) Quantos Produtos Custam mais de 100 Reais ?
C) Qual é o nome do Produto mais Barato ? """
totProduto = prod100 = menor = contador = 0
barato = '  '
print('-'*25)
while True:
    nProduto = str(input('\nQual o nome do produto: '))
    pProduto = float(input('Valor do produto R$: '))
    contador = contador + 1
    totProduto = totProduto + pProduto
    if pProduto >= 100:
        prod100 = prod100 + 1
    if contador == 1:
        menor = pProduto
        barato = menor
    else:
        if pProduto < menor:
            menor = pProduto
            barato = nProduto
        nProduto = nProduto
    continuar = ' '
    while continuar not in 'NS':
        continuar = str(input('Deseja Continuar -> ( S ou N )')).lstrip().upper()[0]
    if continuar == 'N':
        break
print('-'*25)
print(f'Valor Total Gasto na Compra: {totProduto}')
print(f'Quantidade de Produtos acima de R$100,00 -> {prod100} ')
print(f'O produto mais barato -> {barato} e seu preços {menor}')
#print(f'Preços imprimindo{pProduto}')