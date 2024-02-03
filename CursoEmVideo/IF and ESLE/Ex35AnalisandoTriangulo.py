"""DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE 3 RETAS E DIGA O USUARIO
SE ELAS PODEM OU NÃO FORMAR UM TRIANGULO. """

print(30 * '=', '\n',  '    ANALISANDO TRIANGULO \n', 30 * '=')

r1 = float(input('Primeiro segmento: '))
r2 = float (input('Segundo segmento: '))
r3 = float (input('Terceiro segmento: '))

# para formar um triangulo uma reta não pode ser maior do que a soma das outras 2..

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triangulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR ')


