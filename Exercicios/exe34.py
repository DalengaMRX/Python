"""Escreva um programa que pergunte o salário de
um funcionário e calcule o calor do seu aumento.

    Para salários superiores a R$1.250,00, cal - 
cule um aumento de 10%.

    Para os inferiores ou iguais, o aumento é de
15%.
"""
print("")
value = (int(input("Enter your salary: ")))

if value > 1250:
    increase = value * 0.1
    print("")
    print(f"Your salary with the 10% increase is R${ value + increase}\n")
elif value <= 1250:
    increase = value * 00.15
    print("")
    print(f"Your salary with the 15% increase is {value + increase}\n")

print("")
