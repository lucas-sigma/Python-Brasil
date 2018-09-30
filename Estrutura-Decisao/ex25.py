'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    a. "Telefonou para a vítima?"
    b. "Esteve no local do crime?"
    c. "Mora perto da vítima?"
    d. "Devia para a vítima?"
    e. "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

print('Responda com Sim ou Não: ')

a = input("Telefonou para a vítima? ").upper()
b = input( "Esteve no local do crime? ").upper()
c = input("Mora perto da vítima? ").upper()
d = input("Devia para a vítima? ").upper()
e = input("Já trabalhou com a vítima? ").upper()

l = [a, b, c, d, e]
sim = 0

for i in l:
    if i == 'SIM':
        sim += 1

print('Suspeita') if sim == 2 else print('Cúmplice') if sim > 2 and sim < 5 else print('Assassino') if sim == 5 else print("inocente")