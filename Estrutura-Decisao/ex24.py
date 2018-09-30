'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
a. par ou ímpar;
b. positivo ou negativo;
c. inteiro ou decimal.
'''

n1, n2 = input('Digite um número: '), input('Digite outro número: ')
print('\n\ta. par ou ímpar;\n\tb. positivo ou negativo;\n\tc. inteiro ou decimal.')
op = input('Digite a, b ou c para selecionar uma opção: ')

n1, n2 = n1.replace(',', '.'), n2.replace(',', '.')
l1, l2 = n1.split('.'), n2.split('.')

if op.upper() < 'C' or op.upper() > 'A':
    if op.upper() == 'A':
        n1, n2 = int(float(n1)), int(float(n2))
        if n1 % 2 == 0 and n2 % 2 == 0:
            print(f'{n1} e {n2} são pares')
        elif n1 % 2 == 0 and n2 % 2 == 1:
            print(f'{n1} é par e {n2} é ímpar')
        elif n1 % 2 == 1 and n2 % 2 == 1:
            print(f'{n1} e {n2} são ímpares')
        else:
            print(f'{n1} é ímpar e {n2} é par')
    elif op.upper() == 'B':
        n1, n2 = int(float(n1)), int(float(n2))
        if n1 > 0 and n2 > 0:
            print(f'{n1} e {n2} são positivos')
        elif n1 > 0 and n2 < 0:
            print(f'{n1} é positivo e {n2} é negativo')
        elif n1 < 0 and n2 > 0:
            print(f'{n1} é negativo e {n2} é positivo')
        else:
            print(f'{n1} e {n2} são negativos')
    else:        
        if len(l1) == 1 and len(l2) == 1:
            print(f'{n1} e {n2} são inteiros')
        elif len(l1) == 1 and len(l2) > 1:
            print(f'{n1} é inteiro e {n2} é decimal')
        elif len(l1) > 1 and len(l2) == 1:
            print(f'{n1} é decimal e {n2} é inteiro')
        else:
            print(f'{n1} e {n2} são decimais')
else:
    print('Valor inválido.')