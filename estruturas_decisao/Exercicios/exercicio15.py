def classificaçao_de_velocidade():
    velocidade = float(input("Digite a velocidade do veículo (km/h): "))

    if velocidade <= 60:
        print("Velocidade permitida")
    elif 61 <= velocidade <= 80:
        print("Atenção: velocidade acima do permitido")
    else:
        print("Multa por excesso de velocidade")


classificaçao_de_velocidade()