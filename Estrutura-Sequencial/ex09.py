# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).
farenheit = float(input('Temperatura em graus Farenheit: '))
celcius = (5 * (farenheit - 32) / 9)
print('Celsius: ', celcius)