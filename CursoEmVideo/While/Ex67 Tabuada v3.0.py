"""" Faça um programa que mostre a taboada de VARIOS NUMEROS, um de cada vez, para cada valor digitado, pelo usuario, o programa sera
interrompido quando o numero digitado for NEGATIVO."""

''' RODANDO PERFEITAMENTE, ADOREII'''

while True:

    num = int(input('Digite um Numero: '))
    if num <= 0:
        break
    else:
        op = int(input('VAMOS FAZER A TABOADA\n(1) para (X)\n(2) para (//)\n(3) para (+)\n(4) para (-)\nQual a opção: '))
    if op == 1:
        for c in range(1, 11):
            print(f'{num} x {c} = {num * c}')
    elif op == 2:
        for c in range(1, 11):
            print(f'{num} / {c} = {num // c}')
    elif op == 3:
        for c in range(1,11):
            print(f'{num} + {c} = {num + c}')
    elif op == 4:
        for c in range(1, 11):
            print(f'{num} - {c} = {num - c}')
    if num <= 0:
        break


print('PROGRAMA TABOADA ENCERRADO, VOLTE SEMPRE')