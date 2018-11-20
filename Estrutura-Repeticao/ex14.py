'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
'''

n, p1, p2 = [], 0, 0

for i in range(10):
    n.append(int(input('N: ')))
    if n[i] % 2 == 0:
        p1 += 1
    else:
        p2 += 1

print('Pares ==>', p1, '\nImpares ==>', p2)