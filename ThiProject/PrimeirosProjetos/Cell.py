print('_______________________________')
print('______Tabela de Aparelhos:________ ')

a1 = str('Samsung A11')
v1= float(1199)
print('Aparelho: {}  || Valor: {}  || Comissao: {} '.format(a1, v1,v1*15/100))

a2 = ('Samsung A21S')
v2 = float(1399)
print('Aparelho: {}  || Valor: {}  || Comissao: {}'.format(a2, v2, v2*15/100))

a3 = ('Samsung A21S')
v3 = float(1399)
print('Aparelho: {}  || Valor: {}  || Comissao: {}'.format(a3, v3, v3*15/100))

tot = v1+v2+v3

print('--------------------------------------------')
print('VALOR TOTAL: {} \nCOMISSAO: {}'.format(tot,tot*15/100))
print('--------------------------------------------')

ad = float(-1083)#adiantamento
resto = float(120)#Saldo Anterior
compras = float(-150)#Compras da Loja
bonus = float(0)
saldo = ad + resto + compras + (tot*15/100)+bonus
print('--------------------------------------------')
print('COMISSAO: {} \nADIANTAMENTO: {}\nRESTO: {}\nCOMPRAS: {}\nBONUS_GASOLINA: {}\n\nSALDOFINAL: {}'.format(tot*15/100,ad,resto,compras,bonus,saldo))
print('--------------------------------------------')
