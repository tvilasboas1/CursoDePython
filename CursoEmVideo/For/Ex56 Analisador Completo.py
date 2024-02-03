""" Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 Pessoas. No final do programa, mostre:

A media de idade do grupo.

Qual é o nome do homem mais velho.

Quantas mulheres tem menos de 20 anos.

"""
soma = 0
maiorIdade = 0
menosVinte = 0
cont = 0
nomevelho = ''
for c in range(1,5):
    print('------ {}º PESSOA -----'.format(c))
    nome = str(input('Nome: ')).lstrip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[ M / F ]: ')).lstrip().upper()
    soma = idade + soma
    if c == 1 and sexo in 'M':
        maiorIdade = idade
        nomevelho = nome
        print('MaiorIdade na Posição {}'.format(c)) # quando eu retornar nesse exercicio para checar, esse detalhe é o mais importe para entender como o laço trabalha.
    if sexo in 'M' and idade > maiorIdade:
        maiorIdade = idade
        nomevelho = nome
        print('MaiorIdade na Posição {}'.format(c)) # quando eu retornar nesse exercicio para checar, esse detalhe é o mais importe para entender como o laço trabalha.
    if sexo in 'F'  and idade <= 20:
        cont = cont +1

print('------ RESULTADO -----')
print('Foram analisados a IDADE de {} Pessoas\nMedia de IDADE: {} Anos.'.format(c, soma // c))
print('Mulher(s) ate 20 anos: {} '.format(cont))
print('Homem mais velho chama-se: {}\nIdade: {}'.format(nomevelho, maiorIdade))
