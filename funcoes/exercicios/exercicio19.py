def calcular_conta_energia():

    consumo_kwh = float(input("Digite o consumo de energia (em kWh): "))
    preco_kwh = float(input("Digite o preço de cada kWh (R$): "))
    valor_total = consumo_kwh * preco_kwh

    print("\n--- Resumo da Conta de Energia ---")
    print(f"Consumo: {consumo_kwh:.2f} kWh")
    print(f"Preço por kWh: R$ {preco_kwh:.2f}")
    print(f"Valor total a pagar: R$ {valor_total:.2f}")

calcular_conta_energia()