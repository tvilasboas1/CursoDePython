from datetime import datetime
dados = {}
print('--'*15)

dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] =  datetime.now().year - nasc
dados['ctps'] = int(input('N° Carteira de Trabalho. ( 0 = null ): '))


if dados['ctps'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salario'] = float(input('Salario: R$'))
    dados['Aposentadoria'] = dados['idade'] + ((dados['Contratação'] + 35) - datetime.now().year) #35 anos de contribuição foi um exemplo exporadico.
    print('--' * 15)
    for k, v in dados.items():
        print(f'{k} ->> {v}')
else:
    for k, v in dados.items():

        print(f'{k} ->> {v}')
    print('S/ CTPS. Programa encerrado. ')





