def classificaçao_da_nota():

    nota = int(input("Digite a nota de 0 a 10: "))

    if 0 <= nota <= 4:
        print('Insuficiente')
    elif 5 <= nota <= 6:
        print('Regular')
    elif 7 <= nota <= 8:
        print('Bom!')
    elif 9 <= nota <= 10:
        print('Excelente!!')
    else:
        print('Nota Invalida, tente novamente')

classificaçao_da_nota()