"""" Crie um programa que vai ler VARIOS NUMEROS e colocar em uma lista.
Depois disso mostre:

A) Quantos Numeros foram digitados.
B)  A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e esta ou não na lista
"""

valores = []
while True:
    valores.append(int(input('Digite um valor: ' )))
    resp = str(input('Deseja Continuar -> (S / N):  ')).lstrip().upper()

    if resp in 'N':
        break
print(f'Você digitou {len(valores)} elementos\n{valores}')
valores.sort(reverse=True) # Reverse=True vai fazer os valores ficarem em ordem decrescente.
print(f'Os valores em ordem Descrecente: {valores}')
if 5 in valores:
    print('O valor 5 esta na lista...')
else:
    print('O valor 5 não esta na lista')