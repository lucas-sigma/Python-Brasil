# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

n = int(input('Digite um número de 1 a 7: '))

if n >= 1 and n <= 7:
    if n == 1:  print('Domingo')
    elif n == 2:    print('Segunda')
    elif n == 3:    print('Terca')
    elif n == 4:    print('Quarta')
    elif n == 5:    print('Quinta')
    elif n == 6:    print('Sexta')
    else:   print('Sabado')
else:   print('Valor invalido')