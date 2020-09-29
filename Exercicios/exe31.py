"""Desenvolva um programa que pergunte a distância
de uma viagem em km.
    
    Calcule o preço da passagem, combrando R$ 0.50
por km para viagens de até 200km e R$ 0.45 para viagens
mais longas.
"""

print("")

quantity = int(input("Enter the travel distance: "))

if quantity <= 200:

    ticket_value = quantity * 0.50

    print("")
    print(f"The value of your ticket is R${ticket_value} reais")

elif quantity > 200:
    ticket_value = quantity * 0.45

    print("")
    print(f"The value of your ticket is R${ticket_value} reais")

print("")
