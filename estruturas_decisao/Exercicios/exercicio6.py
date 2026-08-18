def maior_ou_menor():

    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))

    if numero1 > numero2:
        print(f'o maior numero é {numero1}')
    elif numero1 < numero2:
        print(f'o maior numero é {numero2}')
    else:
        print('Os numeros sao iguais')

maior_ou_menor()