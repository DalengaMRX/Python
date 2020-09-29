# Faça um algoritmo que leia o salário de um funcionario e 
# mostre seu novo salário, com 15% de aumento.

salario = float(input('Insira o valor do seu salário mensal: '))

aumento = salario * (15/100)
salarioAtual = salario + aumento

print('Seu salario antigo é de: {} Reais'.format(salario))
print('Seu salario atual é de: {} Reais'.format(salarioAtual))