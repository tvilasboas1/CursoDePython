''' Crie uma tupla preechida com os 20 primeiros colocados da tabela do Brasileirao, na ordem de colocação, depois mostre:
a) Apenas os 5 primeiros colocados.
b) Os ultimos 4 colocados na tabela.
c ) Uma lista com os times em ordem alfabetica.
d) Em que posição na Tabela esta o Juventude
''',
print('___'*30)
times = ('Palmeiras', 'Atletico', 'Fortaleza', 'Bragantino', 'AtleticoPR', 'Flamengo', 'Ceara', 'Bahia', 'Fluminense', 'Santos',
         'AtleticoGO', 'Corinthians', 'Internacional', 'Juventude', 'Cuiaba', 'São Paulo', 'Sport', 'AmericaMG', 'Gremio', 'Chapecoense')
print(times)
print('___'*30)
print(f'Os 5 primeiros colocados são {times[0:5]} ')
print('___'*30)
print(f'Os 4 ultimos colocados são {times[-4: ]}') # vai imprimir os quatro ultimos ate o ultimo... Melhor que contar de tals a tals
print('___'*30)
print(f'Em ordem Alfabetica fica {sorted(times)}')
print('___'*30)
print(f'O Juventude esta na posição {times.index("Juventude") + 1}') #Observar as aspas nesse caso é bem importante