''''desenvolva um programa que leia 4 valores pelo teclado e guardeos em uma tupla. No final mostre:
a) Quantas vezes apareceu o valor 9. # usar o count 9
b) Em que posição foi digitado o primeiro valor 3. # index 3
c ) Quais foram os numeros Pares.

'''
# Digite um numero:
# Digite outro numero:
# Digite mais um numero:
# Digite o outro numero:
cont = 'S'

while cont == 'S':
    numero = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')), int(input('Digite um numero: ')))
    print(f'\nOs valores digitados foram: {numero}')
    print(f'O numero 9 foi digitado: {numero.count(9)}x Vezes')
    if 3 in numero:
        print(f'O numero 3 foi digitado na posição: {numero.index(3) + 1} ')
    else:
        print('O numero 3 não foi encontrado.')
    for n in numero:
        if n % 2 == 0:
            print(f'{n } = Par')
    cont = str(input('Deseja Continuar: ')).strip().upper()