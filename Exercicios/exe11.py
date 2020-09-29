# Faça um programa que leia a largura e a  altura de uma pare -
# de em metros, calcule a sua área e a quantidade de tinta ne - 
# cessaria para pinta-la, sabendo que cada litro de tinta, pinta
# uma area de 2m^2 

largura = float(input('Insira a largura da parede em metros: '))
altura = float(input('Insira a altura da parede em metros: '))

area = largura * altura
litros = area / 2

print('A largura da parede é: {} Metros'.format(largura))
print('A Altura da parede é : {} Metros'.format(altura))
print('Sua area é equivalente a: {} Metros quadrados'.format(area))
print('Você precisará de {} Litros de tinta para pintar {} Metros quadrados'.format(litros, area))
