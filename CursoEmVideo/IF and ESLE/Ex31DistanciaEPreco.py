"""CRIE UM PROGRAMA QUE MOSTRE A DISTANCIA DE UMA VIAGEM EM KM. CALCULE O PREÇO DA PASSAGEM,
COBRANDO 0.50 POR KM PARA VIAGENS DE ATE 200KM E 0.45 PARA VIAGENS MAIS LONGAS"""

import random

print('VAMOS FAZER UMA VIAGEM.')
distancia = random.randint(100, 500)
print('A distancia desta viagem: {}Km'.format(distancia))

if distancia <= 200:
    print('Para a distancia de {}KM o valor da viagem = R${}'.format(distancia, (distancia * 0.50)))
else:
    print('Para a distancia de {}KM o valor da viagem tem desconto e fica por = R${}'.format(distancia, (distancia * 0.45)))