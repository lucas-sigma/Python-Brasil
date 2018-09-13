'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
c. A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''

n1, n2, n3 = float(input('Nota 1: ')), float(input('Nota 2: ')), float(input('Nota 3: '))
media = (n1 + n2 + n3) / 3

print(f'Aprovado com Distinção - media {media}') if media == 10 else print(f'Aprovado com media {media}') if media >= 7 else print(f'Reprovado com media {media}')