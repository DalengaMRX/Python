#Fazer um conversor de temperatura de Celsus para
#Fahrenheit

c = float(input('Insira a temperatura em ºC: '))

f = ((c*9)/5) + 32

print('A temperatura {}Cº equivale a {} ºF'.format(c, f))