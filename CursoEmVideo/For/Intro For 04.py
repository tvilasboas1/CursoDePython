#possibilidade de somar e fazer mil coisas.

n = int(input('Digite o Inicio: '))
f = int(input('Digite o Fim: '))
p = int(input('Digite o Pulo: '))

for c in range(n, f+1,p):
    print(c)
print('Fim01')

for c in range(0,3):
    num = int(input('Fala ae um numero: '))
print('Teste Num {}'.format(c)) # aqui quando pede para imprimir, imprime apenas o espaço de repetição que no caso é 2.
print(num) # Aqui esta imprimindo o ultimo numero digitado, so a base de testes mesmo
print('Fim 02')

s = 0
for c in range(0,3):
    n = int(input('Informe outro numero: '))
    s = s + n # ou s=+n
print('Soma = {} '.format(s))
print('Fim03')