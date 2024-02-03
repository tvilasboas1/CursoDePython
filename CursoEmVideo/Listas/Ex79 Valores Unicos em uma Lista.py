"""" Crie um programa onde o usuario possa digitar varios VALORES NUMERICOS e cadastre-os em uma lista. Caso o numero já exista lá dentro,
ele NÃO SERA ADICIONADO. No final, serao exibidos todos os valores unicos digitados em uma ORDEM CRESCENTE"""

numlista = []
c = 0
while True:
    num = int(input('Digite um Numero: '))
    if num not in numlista:
        numlista.append(num)
        if numlista == num:
            numlista = maior = menor
        else:
            if numlista > maior:
                maior = numlista
            if numlista < menor:
                menor = numlista
    else:
        print('Numero já adiconado anteriormente...')
    #numlista.append(int (input('Digite um Numero: ')))
    cont = str(input('\nDeseja digitar outro Nº...: ')).lstrip().upper()
    if cont == 'N':
        break

print(f'Os numeros Informados foram: {numlista}')
numlista.sort()
print(f'Os numeros Informados foram em ORDEM: {numlista}')
print(f'O maior valor digitado: {maior}')
print(f'O menor valor digitado: {menor}')