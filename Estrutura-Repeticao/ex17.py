'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5! = 5.4.3.2.1 = 120
'''

n, fatorial = int(input('Numero: ')), 1

for i in range(n, 1, -1):
    fatorial *= i

print(fatorial)