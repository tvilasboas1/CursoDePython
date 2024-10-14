"""PROGRAMA PARA CALCULAR SE COMPENSA MAIS GASOLINA OU ETANOL"""
et = float(input('Informe o Valor do Etanol: '))
cose = float(input('Informe a autonomia no Etanol: '))
gas = float (input('Informe o valor da Gasolina: '))
cosg = float(input('Informe a autonomia na Gasolina: '))
gasolina = gas / cosg
etanol = et / cose
print('Com Etanol o valor do KM = R${:.2f} por KM'.format(etanol))
print('Com Gasolina o Valor do KM = R${:.2f} por KM'.format(gasolina))