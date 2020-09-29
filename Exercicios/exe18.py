# Faça um programa que leia um angulo qualquer e mostre na 
# tela o valor do seno, cosseno e tangente desse angulo.

from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do angulo: '))

radiano = radians(angulo)

seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print('Seu seno vale {:.2f}'.format(seno))
print('Seu cosseno vale {:.2f}'.format(cosseno))
print('Sua tangente vale {:.2f}'.format(tangente))