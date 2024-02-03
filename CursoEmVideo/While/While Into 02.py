n = 1
par = impar = 0
while n != 0:
    n = int(input('DIGITE UM VALOR: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Voce digitou {} PARES \nVoce digitou {} Impares'.format(par, impar))

print('NOVAMENTE POREM COM OPÇÃO STRING AGORA')
opc= 'S'
pares = 0
impares = 0 #pares = impares = 0
while opc == 'S':
    num = int(input('DIGITE UM NUMERO: '))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    opc = str(input('DESEJA CONTINUAR  [S / N ]: ')).upper()
    if opc == 'S':
        print('Ok, Digite um novo numero: ')
    else:
        print('TOTAL\n{} PARES\n{} IMPARES\nTchau amigo'.format(pares, impares))