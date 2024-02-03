#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade
#de tinta necessaria para pinta-la, sabendo que cada litro pinta uma area de 2 metros quadrados.
alt = float(input('Informe a altura da parede: '))
lar = float(input('Informe a largura da parede: '))
area = alt * lar
print('Area: ',area,"M^2")
print('Para pintar este comodo de {}M^2 é necessario {} de tinta'.format(area,area/2))
