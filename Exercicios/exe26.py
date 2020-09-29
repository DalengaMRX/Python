"""Faça um programa que leia uma frase pelo teclado e mostre:
    
   - Quantas vezes aparece a letra "A".
   - Em que posição ela aparece na primeira vez.
   - Em que posição ela aparece na segunda vez.
"""
print("")

sentence = str(input("Write a phrase: ")).upper()

amount = sentence.count("A")
first_position = sentence.find("A")
last_position = sentence.rfind("A")

print("")

print(f"Phrase: {sentence}\n")

print(f"Your phrase has {amount} 'A'\n")

print(f"The first position of the letter 'A' in your sentence is: {first_position}\n")

print(f"The last position of the letter 'A' in your sentece is: {last_position}\n")