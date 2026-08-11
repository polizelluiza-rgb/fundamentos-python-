def calcular_preco_final(preco, percentual_desconto):

    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return preco_final

preco = float(input("Digite o preço do produto (R$): "))
desconto = float(input("Digite o percentual de desconto (%): "))

valor_com_desconto = calcular_preco_final(preco, desconto)

print(f"O valor final do produto com desconto é: R$ {valor_com_desconto:.2f}")