"""Crie um programa que leia um número inteiro
e mostre na tela se ele é par ou impar.
"""

print("")

number = int(input("Insert a number: "))

if number % 2 == 1:
    print("")
    print("The number is odd")

elif number % 2 == 0:
    print("")
    print("The number is even")

print("")