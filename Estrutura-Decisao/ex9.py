# Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

if n1 > n2 and n1 > n3:
    print(n1)
    if n2 > n3:
        print(n2, '\n', n3)
    else:
        print(n3, '\n', n2)
elif n2 > n1 and n2 > n3:
    print(n2)
    if n1 > n3:
        print(n1, '\n', n3)
    else:
        print(n3, '\n', n1)
else:
    print(n3)
    if n1 > n2:
        print(n1, '\n', n2)
    else:
        print(n2, '\n', n1)  