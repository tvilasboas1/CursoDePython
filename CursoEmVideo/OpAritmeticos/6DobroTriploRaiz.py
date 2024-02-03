#Crie um Algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
n1 = int(input('Informe um numero: '))
tot1 = n1 * 2 # mostrar o dobro
tot2 = n1 * 3 #Mostrar o Triplo
rquad = n1 ** (1/2)

print('Numero informado: {}\nDobro: {}\nTriplo: {}\nRaizQuadrada:{}'.format(n1,tot1,tot2,rquad))