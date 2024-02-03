'''Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de varias pessoas em um dicionario e todos os dicionarios
em uma lista. No final, mostre:

a) Quantas Pessoas Foram Cadastradas.
b) A media de idade do grupo.
c) Uma lista com todas as mulheres.
d) Uma lista com todas as pessoas com idade acima da media. '''
galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome:'] = str(input('INFORME O NOME: '))

    while True:
        pessoa['Sexo:'] = str(input('INFORME O SEXO: ')).upper()[0]
        if pessoa['Sexo:'] in 'MF':
            break
            print('ERRO! Por Favor, Digite Apenas M ou F' )
    pessoa['Idade:'] = int(input('INFORME A IDADE: '))
    soma += pessoa['Idade:']
    galera.append(pessoa.copy())

    while True:
        cont = str(input('Deseja Continuar [S/N]')).upper()[0]
        if cont in 'NS':
            break
            print('Erro. Responda Apenas S ou N')
    if cont == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos um TOTAL de {len(galera)} Pessoas Cadastradas.')
media = soma / len(galera)
print(f'A media de idade é de {media:5.2f} anos. ')
print('As Mulheres Cadastradas Foram:', end='')
for p in galera:
    if p['Sexo:'] == 'F':
        print(f' {p["Nome:"]},', end='')
print()
print('Lista das Pessoas que estão acima da Media: ')
for p in galera:
    if p['Idade:']>= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('<<<ENCERRADO>>>')




