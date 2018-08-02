'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    a. Para homens: (72.7*h) - 58
    b. Para mulheres: (62.1*h) - 44.7
'''
altura = float(input('Digite a altura: '))
pesoIdealHomem = (72.7 * altura) - 58
pesoIdealMulher = (62.1 * altura) - 44.7
print('Peso ideal para homens: ', pesoIdealHomem)
print('Peso ideal para mulheres: ', pesoIdealMulher)