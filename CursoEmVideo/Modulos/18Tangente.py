import math

angulo = float(input ('Informe o valor do angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print ('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print ('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print ('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
