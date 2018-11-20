'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

n = []

for i in range(5):
    n.append(float(input('Numero: ')))

print('Soma: ', sum(n))
print('Media: ', sum(n) / len(n))