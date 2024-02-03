print('Fazendo Fatorial com For...')

num = int(input('Qual o numero a ser calculado ? '))
c = num
fat = 1
for num in range (num, 1, -1):
    fat = fat * c
    c = c - 1
    print('Fatorial de {} x {} = {}'.format(num, c, fat))
print('Fatorial de {}! é = {}'.format(c, fat))



