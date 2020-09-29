""" Crie um programa que leia o nome de uma cidade e 
    diga se ela começa ou não com o nome "SANTO"
"""

cidade = str(input("Insira o nome de qualquer cidade: ")).upper()

lista = cidade.split()
resposta = "SANTO" in lista[0]
print("")
print(f"Nome da cidade digitada: {cidade}\n")
print(f"Sua cidade começa com a palavra SANTOS: {resposta}\n")