# Faça um algoritmo que leia o preço de um produto e mostre seu
# novo preço, com 5% de desconto.

produto = float(input('Insira o valor do produto: '))

desconto = produto * 0.05
precoFinal = produto - desconto

print('O preço do produto normal é: {} Reais'.format(produto))
print('O preço com desconto de 5% é: {} Reais'.format(precoFinal))