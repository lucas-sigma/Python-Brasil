# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print('M - Matutino | V - Vespertino | N - Noturno')
turno = input('Digite o turno em que você estuda: ')
if turno.upper() == 'M':
    print('Bom Dia!')
elif turno.upper() == 'V':
    print('Boa Tarde!')
elif turno.upper() == 'N':
    print('Boa Noite!')
else:
    print('Valor Inválido!')