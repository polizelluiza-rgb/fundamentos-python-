def calcular_consumo_medio():
    distancia = float(input("Digite a distância percorrida (km): "))

    combustivel = float(input("Digite a quantidade de combustível gasta (L): "))

    if combustivel <= 0:
        print("A quantidade de combustível deve ser maior que zero.")
        return

    consumo_medio = distancia / combustivel
    print(f"O consumo médio foi de {consumo_medio:.2f} km/L")
    return consumo_medio

calcular_consumo_medio()