""" Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa
o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario
 senao o emprestimo sera negado."""


casa = float (input('Valor da Casa: R$'))
salario = float (input('Salario Comprador: R$'))
anos = int (input('Quantos Anos de Financiamento?? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos '.format(casa, anos), end='') # End puxa a linha de baixo para cima
print('A pretação sera de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Emprestimo CONCEDIDO')
    else:
    print('Emprestimo NEGADO')