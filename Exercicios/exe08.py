# Escreva um programa que leia um valor em metros e o exiba 
# convertido em centimetros e milimetros.

value = int(input('Insira um numero: '))

cent = value * 100
mili = value * 1000

print('Valor digitado em Metros: {}mt\nValor em Centímetros: {}cm\nValor em milímetros: {}mm'.format(value, cent, mili))