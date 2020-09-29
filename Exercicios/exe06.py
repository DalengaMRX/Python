# Crie um algoritmo que leia um numero e mostre o seu dobro 
# triplo e raiz quadrada.

num = int(input('Insira um número:'))

d = num * 2
t = num * 3
r = num ** (1/2)

print('O numero digitado foi {}\nO seu dobro é {}\nSeu triplo é {}\nE sua raiz quadrada é {}'.format(num, d, t, r))