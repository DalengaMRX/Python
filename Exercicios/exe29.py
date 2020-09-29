"""Escreva um programa que leia a velocidade de um
carro.

    Se ele ultrapassar 80km/h, mostre uma mensagem 
dizendo que ele foi multado.
    
    A multa vai custar R$ 7.00 reais por cada KM 
acima do limite.
"""
print("")

velocity = int(input("Insert the velocity of your car: "))

if velocity > 80:

    difference = velocity - 80
    total_value = float(difference * 7)
    
    print("")
    print(f"!!! SPEED LIMIT EXCEEDED !!!\n")
    print(f"Fine Amount: R${total_value} Reais\n")
else:
    print("")
    print("OKAY\n")
