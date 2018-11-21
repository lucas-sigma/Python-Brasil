'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
'''

n = int(input('N: '))

for i in range(1, n, n+(n-1)):
    print(i)