def classificaçao_de_imc():

    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")


    if imc < 18.5:
        print("Voce esta abaixo do peso")
    elif 18.5 <= imc <= 24.9:
        print("Voce esta no  peso normal")
    elif 25 <= imc <= 29.9:
        print("Voce esta com Sobrepeso")
    else:
        print("Obesidade")

classificaçao_de_imc()