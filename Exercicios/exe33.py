"""Faça um programa que leia 3 números e mostre
qual o maior e qual o menor.
"""

print("")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 == num2 and num2 == num3:
    print(f"All are the same")

elif num1 == num2 and num2 != num3:
    if num2 > num3:
        print(f"The biggest is {num1} and {num2}")
        print(f"The smallest is {num3}")
    else:
        print(f"The biggest is {num3}")
        print(f"The smallest is {num1} and {num2}")

elif num1 == num3 and num3 != num2:
    if num3 > num2:
        print(f"The biggest is {num1} e {num3}")
        print(f"The smallest is {num2}")
    else:
        print(f"The biggest is {num2}")
        print(f"The smallest is {num1} and {num3}")

elif num2 == num3 and num3 != num1:
    if num3 > num1:
        print(f"The biggest is {num2} and {num3}")
        print(f"The smallest is {num1}")
    else:
        print(f"The biggest {num1}")
        print(f"The smallest is {num2} and {num3}")

elif num1 > num2 and num2 > num3:
    print(f"The biggest is {num1}")
    print(f"The smallest is {num3}")

elif num1 > num2 and num2 < num3:
    if num1 > num3:
        print(f"The biggest is {num1}")
        print(f"The smallest is {num2}")
    else:
        print(f"The biggest is {num3}")
        print(f"The smallest is {num2}")

elif num2 > num1 and num1 > num3:
    print(f"The biggest is {num2}")
    print(f"The smallest is {num3}")
    
elif num2 > num1 and num1 < num3:
    if num2 > num3:
        print(f"The biggest is {num2}")
        print(f"The smallest is {num1}")
    else:
        print(f"The biggest is {num3}")
        print(f"The smallest is {num1}")

elif num3 > num1 and num1 > num2:
    print(f"The biggest is {num3}")
    print(f"The smallest is {num2}")
    
elif num3 > num1 and num1 < num2:
    if num3 > num2:
        print(f"The biggest is {num3}")
        print(f"The smallest is {num1}")
    else:
        print(f"The biggest is {num2}")
        print(f"The smallest is {num1}")


