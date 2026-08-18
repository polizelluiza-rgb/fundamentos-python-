def temperatura():

    celsius = float(input("Digite a temperatura em Celsius: "))

    if celsius < 15:
        print('Frio')
    elif 15 <= celsius <= 25:
        print('Agradavel')
    else:
        print('Quente')

temperatura()


