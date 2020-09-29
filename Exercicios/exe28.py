"""Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo com - 
putador.

O programa deverá escrever na tela se o usuário venceu
ou perdeu. 
"""

import random

print("")
print("!!! Guess the number the machine is thinking !!!\n")

num_user = int(input('Enter a number from 0 to 5: '))

num_pc = random.randint(0,5)

if num_user == num_pc:
    print("")
    print(f"Number machine: {num_pc}")
    print(f"Your number: {num_user}\n")
    print("YOU WIN !!!")
else:
    print("")
    print(f"Number machine: {num_pc}")
    print(f"Your number: {num_user}\n")
    print("YOU LOST !!!")