"""Faça um programa que leia um ano qualquer e mostre se ele
é bissexto.
"""

print("")

year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0:
    print("")
    print("Is a leap year")

elif year % 4 != 0 and year % 400 != 0:
    print("")
    print("Is not a leap year")

print("")