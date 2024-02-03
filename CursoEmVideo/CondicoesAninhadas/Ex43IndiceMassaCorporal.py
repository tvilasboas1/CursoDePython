"""" Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule o seu imc e mostre o seu status, de acordo com a tabela abaixo:

Abaixo de 18.5: Abaixo do Peso
Entre 18.5 e 25: Peso ideal
25 ate 30: Sobrepeso
30 ate 40: Obesidade
Acima de 40: Obesidade Morbida"""
print(""" VAMOS CALCULAR O IMC DO POVO:
""")

peso = float(input('Informe o seu peso: '))
alt = float (input('Informe a sua altura: '))
imc = peso / (alt**2)
print(imc)

if imc < 18.5:
    print ('Abaixo do Peso.')
elif  18.5 <= imc <= 25:
    print('Parabéns, peso ideal. ')
elif 25 < imc <= 30: # gostei mais de fazer assim, mas: elif imc > 25 and imc < 30: seria certo e o ideal
    print ('Sobrepeso')
elif 30 >imc <= 40:
    print ('Obesidade')
else:
    print('Obesidade Morbida. ')