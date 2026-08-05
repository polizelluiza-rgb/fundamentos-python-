def calcular_area():
    base = float(input("Digite o valor da base: "))
    altura = float(input("Digite o valor da altura: "))

    area = (base * altura) / 2

    print(f"A área é: {area}")
    return area

calcular_area()