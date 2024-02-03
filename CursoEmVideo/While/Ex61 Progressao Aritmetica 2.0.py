"""" Refaça o DESAFIO 51, lendo o PRIMEIRO TERMO e a RAZAO de uma PA. Mostrando os 10 primeiros termos  da progressao usando a estrutura While"""

a1 = int(input('Digite a A1 (primeiro termo da PA): '))
r = int(input('Informe a Razãao: '))
termo = a1
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end ='' )
    termo = termo + r
    cont = cont + 1


print('Deuuu')