# Exemplo com String Break no campo 3
#
#
cont = 0
while cont <= 10:
    print('{} -> '.format(cont), end='' )
    cont += 1
print('Fim')
print('=' * 60)

#Checando abaixo a F Srings
nome1 = 'Jose'
idade = 21
print(f'O {nome1} possui {idade} anos e pode ficar ainda mais velho com {idade + 1}')

#Ultilizando o Break
num = 0
c = 0
while True:
    num = int(input('Informe um numero [ DIGITE 999 P/ SAIR]'))
    if num == 999:
        break
    else:
        c = c + 1
print(f'Foram digitados {num} que deu um total {c} numeros ')