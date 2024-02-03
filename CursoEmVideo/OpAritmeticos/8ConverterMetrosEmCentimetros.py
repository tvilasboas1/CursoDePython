#Escreva um programa que leia um valor em Metros e o exiba convertido em Centimetros e Milimetros
valor = float(input('Informe quantos METROS: '))
print('Convertendo para centimetros e milimetros')

cent = valor * 100
mil = valor * 1000
print(valor,'M\n{} CM\n{} MM'.format(cent,mil))


