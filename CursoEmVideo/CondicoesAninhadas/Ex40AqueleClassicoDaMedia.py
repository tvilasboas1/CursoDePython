"""Crie um programa que leia duas notas de um aluno e calcule a sua media, mostrando uma mensagem no final, de acordo
com a media atingida:

media abaixo de 5.0: REPROVADO
media entre 5.0 e 6.9: RECUPERAÇÃO
media 7.0 ou Superior: APROVADO """

nota1 = float (input('Informe a N1: '))
nota2 = float(input('Informe a N2: '))
media = (nota1 + nota2 ) / 2

if media < 5.0:
    print('A media do aluno foi baixa {:.2f}. Ele esta REPROVADO. '.format(media))
elif media >= 5.0 and media <= 6.9:
    print('A media do aluno foi {:.2f} e ele esta em  Recuperação'.format(media))
else:
    print('A media do aluno foi {:.2f} e ele esta APROVADO'.format(media))


