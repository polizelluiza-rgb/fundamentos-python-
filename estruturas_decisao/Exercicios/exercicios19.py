def classificaçao_de_numero():
    numero = int(input("Digite um número inteiro: "))

    if numero > 0:
        sinal = "positivo"
    elif numero < 0:
        sinal = "negativo"
    else:
        sinal = "zero"

    if numero % 2 == 0:
        print(f"Classificação: {sinal} e par")
    else:
        print(f"Classificação: {sinal} e ímpar")





classificaçao_de_numero()