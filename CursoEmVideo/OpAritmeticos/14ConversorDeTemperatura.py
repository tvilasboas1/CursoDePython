#conversor de temperatura
('Vamos fazer um conversor de temperatura')
tempf = int(input('Informe a temperatura em graus F: '))
tempc = (tempf - 32) / 1.8
print('A temperatura {}F ao ser convertida para Celsios é = {:.2f}C'.format(tempf,tempc))
