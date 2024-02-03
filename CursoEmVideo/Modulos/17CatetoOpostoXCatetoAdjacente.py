'''co = float (input('Comprimento do Cateto oposto: '))
ca = float (input('Comprimento do Cateto Adjacente'))
hi = (co  **  2 + ca ** 2) ** (1/2)
print ('A hipotenusa vai medir:   {} '.format(hi))'''

from  math import hypot
co = float (input ('comprimento do Cateto Oposto: '))
ca = float (input ('Comprimento do Cateto Adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

math.h