def calcular_perimetro():
    base = float(input("Digite o valor da base: "))
    altura = float(input("Digite o valor da altura: "))

    perimetro = 2 * (base + altura)

    print(f"O perímetro do retângulo é: {perimetro}")
    return perimetro

calcular_perimetro()