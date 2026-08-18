def calculadora_de_frete():
    valor_compra = float(input("Digite o valor da compra (R$): "))

    if valor_compra <= 100:
        frete = 20.0
    elif 101 <= valor_compra <= 300:
        frete = 10.0
    else:
        frete = 0.0

    total = valor_compra + frete

    if frete == 0:
        print(f"Frete grátis! Valor total a pagar: R$ {total:.2f}")
    else:
        print(f"Frete: R$ {frete:.2f} | Valor total a pagar: R$ {total:.2f}")


calculadora_de_frete()