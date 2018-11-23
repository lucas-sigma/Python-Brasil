# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000

n = []

while True:
    i = float(input('N: '))
    if i > 0 and i < 1000:
        n.append(i)
    
    sair = input('Adicionar mais algum valor [S | N]: ')
    if sair.upper() == 'N':
        break

menor, maior, soma = min(n), max(n), sum(n)

print('Menor valor ==>', menor, '\nMaior valor ==>', maior, '\nSoma ==>', soma)