'''
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
'''

x1, x2 = int(input('X1: ')), int(input('X2: '))

for i in range(x1, x2+1):
    print(i)