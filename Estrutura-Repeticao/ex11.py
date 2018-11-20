'''
Altere o programa anterior para mostrar no final a soma dos números.
'''

x1, x2 = int(input('X1: ')), int(input('X2: '))
n = []

for i in range(x1, x2+1):
    print(i)
    n.append(i)

print('\nSoma ==> ',sum(n))