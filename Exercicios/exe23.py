"""Faça um programa que leia um número de 0 a 9999 e mostre 
   na tela cada um dos dígitos separados, descrevendo uni - 
   dade, dezena centena e etc."""

numero = str(input("Insira um número de 0 á 9999: "))

print("")

print("Número digitado: {}\n".format(numero))

print("Milhar: {}\n".format(numero[0]))

print("Centena: {}\n".format(numero[1]))

print("Dezena: {}\n".format(numero[2]))

print("Unidade: {}\n".format(numero[3]))
