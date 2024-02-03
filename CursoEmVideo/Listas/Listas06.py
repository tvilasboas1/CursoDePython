teste = list()
teste.append('Thiago')
teste.append('34')
teste.append('72kg')
print(f'Nome, Idade e Peso: {teste}')
galera = list()
galera.append(teste[:])  # O simbolo de : é para fazer copia, senão a lista é duplicada
teste [0] = 'Maria' # inclusão de dados na lista
teste [1] = 22 # inclusão de dados na lista.
galera.append(teste[:]) # O simbolo de : é para fazer copia, senão a lista é duplicada... Como eu não declarei o teste[2] o sistema manteve os dados da primeira lista.
print(galera)

galera = [['Thiago', 34, '72kg'], ['Maria', 22], ['Carlos', 31, '1.92']]
print(f'Imprimir Galera apos atualizar a lista: {galera}')
print(f'{galera[1][1]}') # Imprimir Apenas Bloco 1 Posição 1
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')  #Imprimindo todos nomes da pos 0 e idades da pos 1
grupao = list()
grupao.append(galera[:])
print(f'Galera entrou no Grupão ? {grupao}')
