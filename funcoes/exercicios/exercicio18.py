def calcular_parcelas():
    valor_produto = float(input("Digite o valor do produto (R$): "))
    qtd_parcelas = int(input("Digite a quantidade de parcelas: "))

    if qtd_parcelas <= 0:
        print("Erro: A quantidade de parcelas deve ser maior que zero.")
        return

    valor_parcela = valor_produto / qtd_parcelas

    print("\n--- Resumo do Pagamento ---")
    print(f"Valor total do produto: R$ {valor_produto:.2f}")
    print(f"Quantidade de parcelas: {qtd_parcelas}")
    print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")

calcular_parcelas()