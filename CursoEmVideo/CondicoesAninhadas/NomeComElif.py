nome = str (input('Qual o seu nome?'))
if nome == 'Thiago':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Jose' or nome == 'Paulo':
    print('Seu nome masculino é bem popular no Brasiill')
elif nome == 'Jessica' or nome == 'Camila' or nome == 'Maria':
    print('Que nome feminino bonito')
else:
    print('tenha um bom dia, {}'.format(nome))
