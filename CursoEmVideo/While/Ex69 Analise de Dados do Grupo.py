"""" Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa devera perguntar se o usuario
quer ou não continuar. No final mostre:

A ) Quantas pessoas tem mais de 18 anos
B ) Quantos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos"""
tot18 = totM = totH = 0
print('==='*25)
while True:
    idade = int(input('\nInforme a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o SEXO: [M ou F] ')).lstrip().upper()[0]
    if idade >= 18:
        tot18 = tot18 + 1
    if sexo == 'M':
        totH = totH + 1
    if sexo == 'F' and idade <=20:
        totM = totM + 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('DESEJA CONTINUAR: (S OU N) ')).lstrip().upper()[0]
    if resp == 'N':
        break
print('==='*25)
print(f'Temos  {tot18} pessoas com mais de 18 anos')
print(f'Temos  {totH} Homens')
print(f'Temos  {totM} Mulheres com menos de 20 anos')