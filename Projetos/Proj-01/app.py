'''
Lendo dados e armazenando na variavel data. Apos isso, eh criada uma variavel listData para criar uma lista com os dados. listData tem seus dados separados por um split.
'''

try:
    data = open('usuarios.txt', 'r')
    listData = []
    listData.append(data.read())
    listData = [i.split('\n') for i in listData]
    data.close()

    # test
    for i in listData:
        if isinstance(i, list):
            for k in i:
                print(k)
    
except IOError:
        print('arquivo nao encontrado!')

'''def formatoRelatorio(arr):
    print('ACME Inc.           Uso do espaço em disco pelos usuários')
    print('------------------------------------------------------------------------')
    print(r'Nr.  Usuário        Espaço utilizado     % do uso\n')
    for i in len(arr):
        print(identificador, '    ', nome, '       ', espacoUtilizado, '            ', percentUso)
    print(f'\nEspaço total ocupado: {totalOcupado} MB')
    print(f'Espaço médio ocupado: {medioOcupado} MB')'''