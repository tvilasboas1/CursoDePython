##Saudaçoes e organização

print('ola mundo!')

nome = input ('Qual é o seu nome amigo:')
print('meu nome é:',nome)
print ('E um prazer conhece-lo Sr', nome)
print ('Prazer em te conhecer {:20}'.format(nome), 'teste espaços') #Aqui estou determinando no numero de espaços
print ('Prazer em te conhecer {:>12}'.format(nome)) #Aqui escreve o nome após saltar os espaços

print ('Prazer em te conhecer{:^25}'.format(nome)) # ele e fica centralizado entre os espaços
print ('Prazer em te conhecer{:.^30}'.format(nome)) #ele usa o ponto ou qualquer outra coisa que e quiser para cobrir espaços em branco



