#Faça um algoritmo que leia o salario de um funcionario e mostre seu nome salario, com 15% de aumento.
print('VAMOS CALCULAR O AUMENTO DO SALARIO DE FUNCIONARIOS')
sal = int(input('Informe o atual salario do colaborador: '))
nsalario = sal + (sal*15/100)
print('O salario atual é {}\nNovo Salario: {}'.format(sal,nsalario))

