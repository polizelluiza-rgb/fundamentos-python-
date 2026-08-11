def calcular_imc():

    peso = float(input("Digite o seu peso em kg (ex: 70.5): "))
    altura = float(input("Digite a sua altura em metros (ex: 1.75): "))

    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")
    return imc

calcular_imc()