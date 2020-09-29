# Faça um programa que leia o comprimento do cateto oposto e 
# do cateto adjacente de um triangulo retangulo, Calcule e 
# mostre o comprimento da hipotenusa. 
from math import hypot

cateto_op = float(input('Informe o cateto oposto: '))
cateto_adj = float(input('Informe o cateto adjacente: '))

result = hypot(cateto_op,cateto_adj)

print('O cateto oposto é {} e o cateto adjacente é {}, logo sua hipotenusa vale {:.2f}'.format(cateto_op,cateto_adj,result))