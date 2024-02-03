""" Crie um programa que leia VARIOS NUMEROS inteiros pelo teclado. No final da execução, mostre a MEDIA ENTRE TODOS os valores
e qual foi o MAIOR e MENOR valores lidos. O programa deve perguntar ao usuario se ele quer ou não CONTINUAR a digitar valores"""
seguir = 'S'
cont = 0
med = float
somador = 0
maior = 0
menor = 0
while seguir != 'N':  #Pode ser tambem... while seguir in 'S':
    num = int(input('Leia um numero: '))

    if seguir == 'S':
        somador = somador + num
        cont = cont + 1

        if cont ==1:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num

    elif seguir == 'N':
        print('SAINDO...')


    seguir = str(input('Deseja Continuar [S / N ]:  ')).upper().strip()[0]
med = somador // cont
print('\nForam digitados {} Numeros.\nA soma entre eles é: {}\nA Media entre eles é: {} '.format(cont, somador, med))
print('Maior Numero Digitado é: {}\nMenor Numero Digitado é: {} '.format(maior, menor))