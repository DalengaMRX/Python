# Faça um programa que leia um numero inteiro e mostre na tela
# o seu sucessor e seu antecessor.

num = int(input('Insira um número: '))

s = num + 1
a = num - 1

print('O Número digitado foi {}\nSeu antecessor é {}\nE seu sucessor é {}'.format(num, a, s))