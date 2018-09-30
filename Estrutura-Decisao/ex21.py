'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1
'''

def numString(num):
    c, d, u = num // 100, num // 10 % 10, num % 10
    
    if c > 0:
        cent = 'uma' if c == 1 else 'duas' if c == 2 else 'três' if c == 3 else 'quatro' if c == 4 else 'cinco' if c == 5 else 'seis' if c == 6 else 'sete' if c == 7 else 'oito' if c == 8 else 'nove' if c == 9 else ''
    if d > 0:
        dez = 'uma' if d == 1 else 'duas' if d == 2 else 'três' if d == 3 else 'quatro' if d == 4 else 'cinco' if d == 5 else 'seis' if d == 6 else 'sete' if d == 7 else 'oito' if d == 8 else 'nove' if d == 9 else ''
    if u > 0:
        uni = 'uma' if u == 1 else 'duas' if u == 2 else 'três' if u == 3 else 'quatro' if u == 4 else 'cinco' if u == 5 else 'seis' if u == 6 else 'sete' if u == 7 else 'oito' if u == 8 else 'nove' if u == 9 else ''

    return cent, dez, uni


print('Saque -- valor minímo: 10 -- valor máximo: 600')
saque = int(input('Valor do saque: '))

#centenas, dezenas, unidades = saque // 100, dezenas // 10 % 10, unidades % 10
centenas, dezenas, unidades = numString(saque)
cOne, dOne, uOne = centenas == 1, dezenas == 1, unidades == 1

cString = f'{cOne} nota de 100' if cOne else f'{centenas} notas de 100'
dString = f'{dOne} nota de 10' if dOne else f'{dezenas} notas de 10'
uString = f'{uOne} nota de 1' if uOne else f'{unidades} notas de 1'

if saque >= 10 and saque <= 600:
    if saque >= 100 and saque <= 600:
        print(f'{cString}, {dString} e {uString}')
    elif saque >= 10 and saque < 100:
        print(f'{dString} e {uString}')
    else:
        print(f'{uString}')
else:
    print('Valor inválido')