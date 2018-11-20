'''
Faça um programa que leia 5 números e informe o maior número.
'''

n = []

for i in range(5):
    n.append(float(input('Numero: ')))

# retorna o maior valor na lista
print(max(n))