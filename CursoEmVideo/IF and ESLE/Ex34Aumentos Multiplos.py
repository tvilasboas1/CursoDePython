"""Escreva um Programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. Para salarios superiores a 1250
calcule aumento de 10%

Para os inferiores ou iguais o aumento é de 15%"""

salario = float(input('Qual é o salario do funcionario ? R$:'))

if salario <=1250:
    novo = salario + (salario * 15 /100)
else:
    novo = salario + (salario * 10 /100)

print( 'Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))
