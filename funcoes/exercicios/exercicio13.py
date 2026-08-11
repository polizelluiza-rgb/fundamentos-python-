def calcular_salario_final(salario_fixo, valor_vendas, percentual_comissao):

    comissao = valor_vendas * (percentual_comissao / 100)
    salario_final = salario_fixo + comissao
    return salario_final

salario_fixo = float(input("Digite o salário fixo (R$): "))
vendas = float(input("Digite o valor total das vendas (R$): "))
percentual = float(input("Digite o percentual de comissão (%): "))

salario_total = calcular_salario_final(salario_fixo, vendas, percentual)

print(f"O salário final do funcionário é: R$ {salario_total:.2f}")