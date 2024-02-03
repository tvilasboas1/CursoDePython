"""" Crie um programa que vai ler VARIOS NUMEROS e colocar em uma lista.

Depois disso, crie duas listas extras que vão conter apenas os valores PARES e os IMPARES digitados, respectivamente.

Ao final mostre o conteudo das TRES LISTAS geradas"""

valores = list()
par = list()
impar = list()
numeros = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    opc = str(input('Deseja Digitar um Novo Numero: [ S ou N ] -> ')).lstrip().upper()
    if opc == 'N':
        break
for i, v in enumerate(valores):
    """print(f' do i {i}') # contador que começa em Zero é vai 0,1,2,3...
    print(f' do i {v}')#aqui vai imprimindo cada numero separado ate fazer toda a lista
    print(f' do i {valores}')# aqui imprive a lista a quantidade de vezes que foi pedido"""
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'Os valores listados na lista foram: {valores}')
print(f'Valores Pares da Lista {par}')
print(f'Valores Impares da Lista {impar}')