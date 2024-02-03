print('A outra forma de fazer....')

n = int(input('Digite um número entre 0 e 9999: '))
v = str(n+10000)
print("""VALOR DA UNIDADE: {}
VALOR DA DEZENA: {}
VALOR DA CENTENA: {}
VALOR DA MILHAR: {}""".format(v[4],v[3],v[2],v[1]))
