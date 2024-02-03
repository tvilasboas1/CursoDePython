"""" Melhore o Desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 TERMOS"""

a1 = int(input('Digite a A1 (primeiro termo da PA): '))
r = int(input('Informe a Razãao: '))
termo = a1
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:

        print('{} -> '.format(termo), end ='' )
        termo = termo + r
        cont = cont + 1
    print('Pausa')
    mais = int(input('Quantos Termos você quer mostrar: '))
print('Fim')
