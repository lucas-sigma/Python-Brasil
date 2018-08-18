# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

tamanho = int(input('Digite o tamanho em metros quadrados da área: '))
cobertura = tamanho / 3
latas = int(cobertura // 18)
if latas < 1:
    latas = 1

print('Quantidade de latas: ', latas)
print('Preço total: ', latas * 80.00, 'R$')