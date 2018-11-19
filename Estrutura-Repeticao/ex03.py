'''
Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; 
'''

while True:
    nome      =  input('Nome: ')
    idade     =  int(input('Idade: '))
    salario   =  float(input('Salario: '))
    sexo      =  input('Sexo: ')
    estCivil  =  input('Estado civil: ')

    if (len(nome) > 3) and (idade > 0 and idade < 150) and (salario > 0) and (sexo.upper() == 'F' or sexo.upper() == 'M') and (estCivil.upper() == 'S' or estCivil.upper() == 'C' or estCivil.upper() == 'V' or estCivil.upper() == 'D'):
        break