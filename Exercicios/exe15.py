#Escreva um programa que pergunte a quantidade de KM
#percorrido por um carro alugado e a quantidade de 
#dias pelos quais ele foi alugado. Calcule o preço 
# a pagar. Calcule o preço a pagar sabendo que o carro
#custa 60 reais por dia e 0,15 centavos por kilometros
# rodados.

k = float(input("Informe a quantidade de KM percorrido: "))
d = float(input("Informe a quantidade de dias alugado: "))

km = 0.15
dia = 60

total_km = k * km
total_dia = d * dia
total_pago = total_dia + total_km
#ou
# total = ((k * 0.15) + (d * 60))

print("O valor total a pagar é de R${:.2f} reais.".format(total_pago))
