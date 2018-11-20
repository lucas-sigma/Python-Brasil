'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''

# c eh responsavel por calcular os anos necessarios para A >= B
a, b, c = 80000, 200000, 0

while a < b:
    a *= 1.03
    b *= 1.015
    c += 1
    #print('A ==>', a, ' \tB ==>', b)

print(c)