""" Faça um programa que calcule a soma entre todos os numeros impares que são multiplos de 3 e que se encontram no intervalo de 1 ate 500."""

print('VAMOS AOS IMPARES MULTIPLOS DE 3:')
soma = 0
cont = 0
for c in range(3,500 + 1,6): # usando o 6 porque ai ele vai imprimir apenas os numeros pares
    soma = soma + c
    cont = cont + 1
    print('E impar & Multiplo de 3: {}'.format(c))
print('A soma de todos valores solicitados é = {} e foram contados: {} numeros'.format(soma, cont))
print('Fim da Contagem')