# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Digite uma letra: ')
invalida = not letra.isalpha()
marca = letra.upper()
vogal = marca[0] == 'A' or marca[0] == 'E' or marca[0] == 'I' or marca[0] == 'O' or marca[0] == 'U'
print('Digite apenas letras!') if invalida else print('Vogal') if vogal else print('Consoante')