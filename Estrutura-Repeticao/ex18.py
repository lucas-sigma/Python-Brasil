'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''

n = []

while True:
    n.append(float(input('N: ')))
    
    sair = input('Adicionar mais algum valor [S | N]: ')
    if sair.upper() == 'N':
        break

menor, maior, soma = min(n), max(n), sum(n)

print('Menor valor ==>', menor, '\nMaior valor ==>', maior, '\nSoma ==>', soma)