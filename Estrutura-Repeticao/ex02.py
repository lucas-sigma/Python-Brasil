# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 

user, password = input('user: '), input('password: ')

while(user.upper() == password.upper()):
    user, password = input('user: '), input('password: ')