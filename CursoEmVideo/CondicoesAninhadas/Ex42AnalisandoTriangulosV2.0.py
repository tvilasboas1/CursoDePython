"""" Refaça o Desafio 035 dos triiangulos, acrescentando o recurso de monstrar que tipo de triangulo sera formado:

Equilatero: todos lados iguais
Isosceles: Dois lados iguais
Escaleno: Todos os lados diferentes"""

print(30 * '=', '\n',  '    ANALISANDO TRIANGULO \n', 30 * '=')

r1 = float(input('Primeiro segmento: '))
r2 = float (input('Segundo segmento: '))
r3 = float (input('Terceiro segmento: '))

if r1 == r2 == r3: # Phyton permite cortar caminho, perfeito.
    print('TRIANGULO EQUILATERO')
elif r1 == r3 or r1 == r2 or r2 == r3: # ou também r1 != r2 != r3 != r1:   " Assim vai rodar... != é o simbolo de DIFERENTE
    print ('TRIANGULO ISOSCELES')
else:
    print('TRIANGULO ESCALENO')