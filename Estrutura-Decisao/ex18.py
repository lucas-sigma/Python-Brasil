# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

def dateValidate():
    date = input('Digite uma data no formato dd/mm/aaaa: ')
    listDate = date.split('/')

    if len(date) == 10 or len(date) == 9 or len(date) == 8:
        if len(listDate[0]) == 2 or len(listDate[0]) == 1:
            day = int(listDate[0])
            if day > 0 and day < 32:
                if len(listDate[1]) == 2 or len(listDate[1]) == 1:
                    month = int(listDate[1])
                    if month > 0 and month < 13:
                        if len(listDate[-1]) == 4:
                            year = int(listDate[-1])
                            if year > 0 and year < 10000:
                                return 'Data válida.'
    return 'Data inválida'

if __name__ == '__main__':
    x = dateValidate()
    print(x)