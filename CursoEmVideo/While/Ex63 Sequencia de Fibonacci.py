"""" Escreva um programa que leia um NUMERO N inteiro qualquer é mostre na tela os N primeiros elementos de uma
sequencia de Fibonacci

Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8"""

num = int(input('Quantoas termos voce quer mostrar ??  '))
t1 = 0
t2 = 1
cont = 3 # porque já mostrou a soma dos 2 primeiros numeros, não tem sentido o contador começar em menos

print('{} -> {} -> '.format(t1, t2), end='')
while cont <= num:

    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    t1 = t2 #T1 passa a ser T2
    t2 = t3 #T2 passa a ser T3 e assim vai andando
    cont = cont + 1
print('Fim da Contagem')