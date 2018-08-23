# Faça um Programa que leia três números e mostre o maior deles.
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

print(n1) if n1 > n2 and n1 > n3 else print(n2) if n2 > n1 and n2 > n3 else print(n3)