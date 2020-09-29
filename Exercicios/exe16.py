# Crie um programa que leia um número real qualquer pelo 
# teclado e mostre na tela sua porção inteira.

from math import floor

num = float(input('Digite um número: '))

print('O numero digitado foi {} e a porção inteira do número é {}'.format(num, floor(num)))