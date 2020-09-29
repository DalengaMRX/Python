# 004_Faça um progrma que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possiveis sobre ele

word = input('Digite algo: ')

print('Digitado: {}'.format(word))
print('seu tipo primitivo é: {}'.format(type(word)))
print('É um numero: {}'.format(word.isnumeric()))
print('Contém espaço: ',word.isspace())
print('É maiúscula: {}'.format(word.isupper()))
print('É minúscula: ', word.islower())