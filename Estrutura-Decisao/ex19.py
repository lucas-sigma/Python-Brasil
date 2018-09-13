'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
* 326 = 3 centenas, 2 dezenas e 6 unidades
* 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

n = int(input('Digite um número inteiro menor do que 1000: '))
c, d, u = n // 100, n // 10 % 10, n % 10
cOne, dOne, uOne = c == 1, d == 1, u == 1
cString, dString, uString = 'centena' if cOne else 'centenas', 'dezena' if dOne else 'dezenas', 'unidade' if uOne else 'unidades'

if n < 1000:
    if n > 100:
        print(f'{c} {cString}, {d} {dString} e {u} {uString}')
    if n < 100 and n > 10:
        print(f'{d} {dString} e {u} {uString}')
    elif n < 10:
        print(f'{u} {uString}')
else:
    print('Valor invalido.')
