#Neste caso sera feito usando listas

aluno = []
nome = str(input('Informe o Nome: '))
nota1 = float(input('Informe a N1: '))
nota2 = float(input('Informe a N2: '))
media = (nota1 + nota2) / 2

aluno.append([nome, [nota1, nota2]])
aluno.append([media])
print(f'Aluno & Notas ->  {aluno[0]}\nMedia -> {aluno[1]}')
if media >= 60.0:
    print('O ALUNO ESTA APROVADO')
else:
    print('ALUNO REPROVADO')



