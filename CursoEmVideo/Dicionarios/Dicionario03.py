#Pode criar uma lista, uma tupla e um dicionario tudo junto.
brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print('--' * 15)
print(f'Imprimindo estado01{estado1}')
print(f'Imprimindo estado02{estado2}')
print('--' * 15)
print(brasil) #imprime os dois dicionarios da lista
print(f'Imprimir Brasil[0] {brasil[0]} ') # ou seja vai imprimir o estado 01 pois ele foi o primeiro inclemento na lista
print('--' * 15)

#Ou sendo mais especifico
print(brasil[0]["UF"])
print(f'Imprimir a sigla do dicionario dentro da lista: ->>   {brasil[1]["Sigla"]}') #a digitação tem que bater exatamente como foi colocada no dicionario.


