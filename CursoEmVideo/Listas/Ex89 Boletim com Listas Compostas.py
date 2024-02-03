"""" Crie um programa que leia NOME e DUAS NOTAS de varios alunos e guarde tudo em uma LISTA COMPOSTA. No final, mostre um
boletim contendo a MEDIA de cada um e permita que o usuario possa mostrar as notas de cada aluno individualmente.

exemplo: NA HORA DE FAZER ESSE EXERCICIO VER O VIDEO DA AULA 18 PARA VER FUNCIONANDO. """

ficha = list()
while True:
    nome = str(input('Informe o Nome: '))
    nota1 = float(input('Informe a N1: '))
    nota2 = float(input('Informe a N2: '))
    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])

    resp = str(input('Cadastrar Novo Aluno [S/N] ->  ')).lstrip().upper()
    if resp in 'Nn':
        break

print('--' * 20)
print(f'{"N°":<4}{"NOME":<10}{"MEDIA":>8}') # ficar atento as Strings formatadas.
print('-' *25)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*25)
    opc = int(input('N° do Aluno P/ Mostrar as Notas: Press 999 to EXIT'))
    if opc == 999:
        print('Finalizando....')
        break
    if opc <= len(ficha):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

print('VOLTE SEMPRE...')