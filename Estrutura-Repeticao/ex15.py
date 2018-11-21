'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
'''

n = int(input('N: '))
n1, n2 = 0, 1

for i in range(n):
    print(n1)
    print(n2)
    n1 += n2
    n2 += n1