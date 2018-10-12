def leitura():
    try:
        data = open('usuarios.txt', 'r')
        print(data)
    except IOError:
        print('arquivo nao encontrado!')

def formatoRelatorio(arr):
    print('ACME Inc.           Uso do espaço em disco pelos usuários')
    print('------------------------------------------------------------------------')
    print(r'Nr.  Usuário        Espaço utilizado     % do uso\n')
    for i in len(arr):
        print(identificador, '    ', nome, '       ', espacoUtilizado, '            ', percentUso)
    print(f'\nEspaço total ocupado: {totalOcupado} MB')
    print(f'Espaço médio ocupado: {medioOcupado} MB')