#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
print('Comprando um produto c/ desconto')
prod = float(input('Informe o valor do produto: '))
desc = prod - (prod * 0.05)
print('Valor do Produto: {}\nValor com Desconto: {}'.format(prod,desc))