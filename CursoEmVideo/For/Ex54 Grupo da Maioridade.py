""" Crie um programa que leia o ANO DE NASCIMENTO de Sete Pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores."""
from datetime import date
print('Hoje é dia {}'.format(date.today()))
dataHoje = date.today().year
menor = 0
maior = 0
cont = 0
for c in range(1, 7):
    nasc = int(input('Informe o ano de Nascimento da {}º Pessoa: '.format(c)))
    data = dataHoje - nasc
    if data >= 18:
        maior = maior + 1
    elif data < 18:
        menor = menor + 1
    cont = cont + 1
print('Neste Grupo foram ANALISADOS:  {} Pessoas.\nMaiores de Idade: {}\nMenores de Idade: {}'.format(cont, maior, menor))
