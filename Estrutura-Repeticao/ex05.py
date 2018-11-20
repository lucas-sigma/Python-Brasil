'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''

a, b, c = float(input('Populacao inicial A: ')), float(input('Populacao inicial B: ')), 0
taxaCrescimentoA, taxaCrescimentoB = float(input('Taxa de crescimento A: ')), float(input('Taxa de crescimento B: ')),

while a < b:
    a *= taxaCrescimentoA
    b *= taxaCrescimentoB
    c += 1
    #print('A ==>', a, ' \tB ==>', b)

print(c)