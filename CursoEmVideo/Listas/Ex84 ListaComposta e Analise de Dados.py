""" Faça um programa que leia o NOME E PESO de VARIAS PESSOAS, guardando tudo em uma lista. No final, mostre:

a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves.


Exemplo ->

nome: Maria
Peso: 70
Quer Continuar ? [S/N]

nome: João
Peso: 100
Quer Continuar ? [S/N]

nome: Claudio
Peso: 85
Quer Continuar ? [S/N]

nome: Helio
Peso: 100
Quer Continuar ? [S/N]

nome: Ana
Peso: 70
Quer Continuar ? [S/N]

nome: Gustavo
Peso: 88
Quer Continuar ? [S/N]
___________________________________________________
Ao tod vc cadastrou 6 pessoas.
O maior peso foi de 100kg. Peso de Joao Helio
O menor peso foi de 70kg. Peso de Maria Ana

"""
dados = list()
pessoas = list()
maiorPeso = 0
menorPeso = 0
pe = 0
while True:
    dados.append(str(input('Informe o nome: ')))
    dados.append(float(input('Informe o Peso: ')))

    if len(pessoas) == 0: # len é para fazer a contagem... So funcionou com a variavel principal
        maiorPeso = menorPeso = dados[1] # só funcionou usando dados. Quando se usa pessoas acaba não dando certo
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]

    pessoas.append(dados[:])
    dados.clear()
    pe = pe + 1
    resp = str(input('Deseja Continuar -> (S / N):  ')).lstrip().upper()
    if resp in 'N':
        break
print( 35 * '++')
print(f'Quantidade de Pessoas [Usando LEN]: {len(pessoas)}')
print(f'Quantidade de Pessoas c/ contador PE: {pe}')
print(f'Pessoas: {pessoas} ')
print(f'MaiorPeso =  {maiorPeso}Kg -> ',  end='' )
for p in pessoas:
    if p[1] == maiorPeso:
        print(f'{p[0]}')
print(f'MenorPeso {menorPeso}Kg -> ',  end='')
for p in pessoas:
    if p[1] == menorPeso:
        print(f'{ p[0]}')





