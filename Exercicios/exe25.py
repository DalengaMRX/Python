"""Crie um programa que leia o nome de uma pessoa e diga se
   ela tem "SILVA" no nome.
"""
print("")
name = str(input("Writer your name: ")).upper()

answer = "SILVA" in name

print("")

print(f"Your name: {name}\n")

print(f"Your name has SILVA: {answer}\n")