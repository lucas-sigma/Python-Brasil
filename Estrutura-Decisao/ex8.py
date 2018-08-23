# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

n1 = int(input('Valor do primeiro produto: '))
n2 = int(input('Valor do segundo produto: '))
n3 = int(input('Valor do terceiro produto: '))

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3
print(menor)