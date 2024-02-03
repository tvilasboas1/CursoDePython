'''' Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar 999, que é a condição
de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles ( desconsiderando o flag )'''

num = 0
c = 0
s = 0
while True:
    num = int(input('Informe um numero [ DIGITE 999 P/ SAIR]: '))
    if num == 999:
        break
    else:
        c = c + 1
        s = s + num
print(f'Foram digitados {c} numeros. \nA soma entre os numeros é = {s} ')
