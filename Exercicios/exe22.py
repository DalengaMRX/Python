"""Crie um programa que leia o nome completo de uma pessoa
   e mostre:
   
   - O nome com todas as letras maiúsculas.
   - O nome com todas minúsculas.
   - Quantas letras ao todo (Sem considerar espaços).
   - Quantas letras tem o primeiro nome.
"""
print("")
nome = str(input("Insira seu nome COMPLETO: "))

space = nome.count(" ")
index = len(nome)

split_nome = nome.split()

print("")
print("Todas as letras maiúsculas: ", nome.upper())
print("")
print("Todas as letras minúsculas: ", nome.lower())
print("")
print("Total de letras (Sem espaço): ", (index - space))
print("")
print("Quantas letras possui seu primeiro nome: ", len(split_nome[0]))
