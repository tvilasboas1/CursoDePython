""""Crie um programa que simule o funcionamento de um Caixa Eletronico. No inicio, pergunte ao usuario qual sera o valor a ser sacado
(numero inteiro )
e o programa vai informar quantas cedulas de cada valor serao entregues

Obs: Considere que o Caixa Possui cedulas de R$50. R$20. R$10 e R$2 """
print('='*30)
print('{:^30}'.format('BANCO TIH'))
print('='*30)
valorsacar = int(input('Valor a ser sacado: '))
total = valorsacar
ced = 50
totced = 0
while True:
    if total >= ced:
        total = total - ced
        totced = totced + 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
            totced = 0
        if total == 0:
            break
