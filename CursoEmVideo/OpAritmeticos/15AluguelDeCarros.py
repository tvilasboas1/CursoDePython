#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
print("Locadora de Veiculos")
km = int (input('Qual a quantidade de KM que rodou no veiculo: '))
dias = int (input('Quantos dias o veiculo ficou locado: '))
tot = (km * 0.15) + (dias * 60)
print('Veiculo locado por: {} dias\nRodando {} KM\nValor Total: {:.0f}'.format(dias,km,tot))