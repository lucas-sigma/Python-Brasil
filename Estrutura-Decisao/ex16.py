'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''
from math import sqrt

a, b, c = float(input('a: ')), float(input('b: ')), float(input('c: '))
delta = b ** 2 - 4 * a * c
x1, x2 = (-b + sqrt(delta))/(2*a), (-b - sqrt(delta))/(2*a)

if a == 0:
    print('Equação não é do segundo grau.')
else:
    if delta < 0:
        print('Equação não possui raízes reais.')
    elif delta == 0:
        print(f'Equação com apenas uma raíz real: {x1}')
    else:
        print(f'A equação possui duas raízes reais:\n\t{x1}\n\t{x2}')
