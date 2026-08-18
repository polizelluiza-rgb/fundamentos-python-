def calcular_desconto():

    valor = float(input("Digite o valor da compra (R$): "))

    if valor <= 100:
        desconto_porcentagem = 0
        print('Sem desconto aplicado')
    elif 101 <= valor <= 500:
        desconto_porcentagem = 10
    else:
        desconto_porcentagem = 15


    valor_desconto = valor * (desconto_porcentagem / 100)
    valor_final = valor - valor_desconto

    print(f"Desconto aplicado: {desconto_porcentagem}% (R$ {valor_desconto:.2f})")
    print(f"Valor final a pagar: R$ {valor_final:.2f}")



calcular_desconto()

