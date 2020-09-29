"""Faça um programa que leia o nome completo de uma pessoa, mostrando
   em seguida o primeiro e o último nome separadamente.
"""
print("")
name = str(input("Write your name: ")).upper()

name_list = name.split()
first_name = name_list[0]
inverted_list = name_list[::-1] 
last_name = inverted_list[0]

print("")

print(f"Your name: {name}\n")

print(f"Your first name is: {first_name}\n")

print(f"Your last name is: {last_name}\n")