"""Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem ou
não formar um triângulo.
"""
print("")

line_a = int(input("Enter the size line A: "))
line_b = int(input("Enter the size line B: "))
line_c = int(input("Enter the size line C: "))

print("")

if (line_b - line_c) < line_a < (line_b + line_c) and (line_a - line_c) < line_b < (line_a + line_c) and\
    (line_a - line_b) < line_c < (line_a + line_b):
    print("The three lines can form a triangle\n")

else:
    print("The three lines cannot form a triangle\n")
