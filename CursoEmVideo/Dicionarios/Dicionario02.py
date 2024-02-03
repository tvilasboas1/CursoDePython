#vamos ao exemplo de um FILME com dicionarios ( Estrutura de Dados )
#movie = dict()
movie = {'Titulo' : 'Star Wars','Diretor' : 'Geoge Lucas','Ano':'1977'}
print(movie)
print('--'*20)
print(movie.values()) # retorna todos os valores do Dicionario.
print(movie.keys())#são as chaves, vai pegar 'Titulo', 'Diretor', 'Ano'
print(movie.items())#vai pegar tudo.

print('----- USANDO O LAÇO-------')
#usando o laçoo
for k, v in movie.items():
    print(f'O {k} é {v}')