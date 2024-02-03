dados = dict() #ou dados={}
dados = {'nome': 'Pedro', 'idade':'25','sexo':'Masculino'}
print(dados['nome'])
print(dados['idade'])
print(dados['sexo'])
print('--' * 20)

#é possivel incluir novos dados dentro do dicionario
dados['altura'] = '1.72'
print(dados['altura'])
print(dados)
print('--' * 20)

#é possivel excluir dados dentro do dicionario
del dados['idade']
print(dados)

#usando a formatação
print(f'O {dados["nome"]} possui {dados["altura"]}m de Altura') #No print formatado tem que usar aspas duplas
